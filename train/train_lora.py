"""
Training
"""
import os

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
from trl import SFTTrainer
import torch

from models import mistral_7b_0  # put base model path in models.py

# base model and dataset
base_model = mistral_7b_0
dataset_name = "mlabonne/guanaco-llama2-1k"

# where to save the model
model_save_path = ""  # put save path here
os.makedirs(model_save_path, exist_ok=True)

# easy going on memory: 4bit-config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,  # better compression
)

# load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(
    base_model,
    trust_remote_code=True
)
tokenizer.pad_token = tokenizer.eos_token

# LoRA-config
model = prepare_model_for_kbit_training(model)
peft_config = LoraConfig(
    lora_alpha=32,  # higher for better performance
    lora_dropout=0.05,
    r=16,  # higher for more parameters
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=[  # more modules
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj"
    ]
)
model = get_peft_model(model, peft_config)

# training setup
training_arguments = TrainingArguments(  # training parameters
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,  # batch-Size: 8
    learning_rate=1e-4,
    warmup_steps=100,
    weight_decay=0.01,
    fp16=False,
    bf16=True,
    save_steps=50,
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=50,
    save_total_limit=3,  # keep 3 checkpoints
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    report_to=None,
    dataloader_drop_last=True,
    remove_unused_columns=False,
)

# load and prepare dataset
dataset = load_dataset(dataset_name, split="train")

# split for validation
train_dataset = dataset.select(range(int(len(dataset) * 0.9)))
eval_dataset = dataset.select(range(int(len(dataset) * 0.9), len(dataset)))

# build trainer and start training
trainer = SFTTrainer(
    model=model,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,  # validation
    peft_config=peft_config,
    args=training_arguments,
    #tokenizer=tokenizer,
    #max_seq_length=512,  # limit sequence length
    #dataset_text_field="text",
)

# print trainable parameters
def print_trainable_parameters(model):
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"Trainable params: {trainable_params:,d} || \
        All params: {all_param:,d} || \
        Trainable%: {100 * trainable_params / all_param:.2f}"
    )

print_trainable_parameters(model)

# run training
try:
    trainer.train()
    trainer.model.save_pretrained(model_save_path)
    tokenizer.save_pretrained(model_save_path)
    print(f"Model saved to {model_save_path}")

except Exception as e:
    print(f"Training failed: {e}")
