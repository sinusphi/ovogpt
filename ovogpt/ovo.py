"""oVoGPT"""
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
import torch
from pages import chat_page
from tokens import account_token  # put your token in tokens.py
#from secret_tokens import my_secret_token
#token = account_token if len(account_token) > 0 else my_secret_token
token = account_token


HTML = chat_page

app = Flask(__name__)


# initialize model
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3"
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    token=token,
    cache_dir="G:/.huggingface_cache"
)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    token=token,
    cache_dir="G:/.huggingface_cache"
).cuda()


def call_mistral(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=128)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply


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
