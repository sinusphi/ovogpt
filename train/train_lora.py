"""Training"""
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
from models import mistral_7b_0
#from secret_models import secret_mistral_7b_0
#model = mistral_7b_0 if len(mistral_7b_0) > 0 else secret_mistral_7b_0
model = mistral_7b_0


# base model and dataset
base_model = model
dataset_name = "mlabonne/guanaco-llama2-1k"


# easy going on memory: 4bit-config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=False
)


# load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16
)
tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token


# LoRA-config
model = prepare_model_for_kbit_training(model)
peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.1,
    r=8,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj"]
)
model = get_peft_model(model, peft_config)


# parameters for training
training_arguments = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,
    learning_rate=2e-4,
    fp16=True,
    bf16=False,
    save_steps=25,
    logging_steps=25,
    report_to=None
)


# load dataset
dataset = load_dataset(dataset_name, split="train")


# build trainer and start training
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    args=training_arguments
)


trainer.train()
trainer.model.save_pretrained("./mistral_7b_custom_lora")
