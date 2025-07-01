"""
oVoGPT
"""
import threading
import webbrowser
import time

from flask import (
    render_template_string,
    Flask,
    jsonify,
    request,
)
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch

from pages import chat_page
from tokens import account_token  # put your token in tokens.py



HTML = chat_page

app = Flask(__name__)

base_model_path = ""     # path to the base model
lora_model_path = ""     # path to the lora custom model
lora_output_path = ""    # lora output path
cache_dir = ""           # huggingface save directory


# initialize tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    base_model_path,
    token=account_token,
    cache_dir=cache_dir
)

# add padding token if missing
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# initialize base model
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_path,
    torch_dtype=torch.float16,
    token=account_token,
    cache_dir=cache_dir,
    device_map="auto"  # auto device mapping
)

# load lora adapter on top of base model
model = PeftModel.from_pretrained(
    base_model,  # pass the loaded model
    lora_model_path
)


def call_mistral(prompt):
    try:
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        # move inputs to the same device as model
        device = next(model.parameters()).device
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=128,
                do_sample=True,
                temperature=0.7,
                pad_token_id=tokenizer.eos_token_id
            )

        # decode only the new tokens (exclude the input prompt)
        new_tokens = outputs[0][len(inputs['input_ids'][0]):]
        reply = tokenizer.decode(new_tokens, skip_special_tokens=True)
        return reply.strip()

    except Exception as e:
        print(f"Error in call_mistral: {e}")
        return f"Error: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    question = None

    if request.method == 'POST':
        question = request.form['frage']
        answer = call_mistral(question)

    return render_template_string(HTML, antwort=answer, frage=question)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get("frage", "")
    answer = call_mistral(question)
    return jsonify({"antwort": answer})


def open_browser():
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000')



if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run(host='127.0.0.1', port=5000)
