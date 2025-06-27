import requests
import threading
import webbrowser
import time
from flask import (
    render_template_string,
    Flask,
    jsonify,
    request,
)
from pages import chat_page


HTML = chat_page

app = Flask(__name__)


# ollama api endpoint and model name
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"  # alternatives: mistral, llama3, gemma, ...


# call the local ollama server with a prompt and get a response
def call_ollama(prompt):
    response = requests.post(OLLAMA_ENDPOINT, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    if response.ok:
        return response.json().get("response", "").strip()

    return "[error contacting llm]"


@app.route('/', methods=['GET', 'POST'])
def index():
    # initialize variables for user question and model answer
    answer = None
    question = None
    if request.method == 'POST':
        question = request.form['frage']  # get user's question
        answer = call_ollama(question)  # generate a response
    # render the html page
    return render_template_string(HTML, antwort=answer, frage=question)


@app.route('/chat', methods=['POST'])
def chat():
    # get the incoming json data (key 'frage' is expected)
    data = request.json
    question = data.get("frage", "")
    answer = call_ollama(question)  # generate a response
    return jsonify({"antwort": answer})  # return answer as json


def open_browser():
    # wait for server ready
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000')



if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run(host='127.0.0.1', port=5000)  # launch the server
