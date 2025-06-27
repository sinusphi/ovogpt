oVoGPT
******

**A simple demo for running language models locally and securely.**

.. image:: https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=FFE873
    :target: https://www.python.org/downloads

.. image:: https://img.shields.io/badge/code%20style-black-000000
    :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/donations-paypal-orange?logo=paypal&logoColor=darkblue
    :target: https://paypal.me/yserestou

|

.. image:: https://github.com/sinusphi/ovogpt/blob/main/ovogpt/static/screen1.png?raw=true

|

Beschreibung
------------

oVoGPT (Our Very Own GPT) ist eine leichtgewichtige Demo-Anwendung, mit der 
sich ein Sprachmodell, ähnlich wie ChatGPT, direkt auf dem eigenen Computer 
oder Server betreiben lässt. Eine Internetverbindung ist nicht erforderlich, 
sämtliche Daten werden lokal verarbeitet und verlassen das System zu keinem 
Zeitpunkt.

Diese Demo wurde entworfen um sowohl Technik-Interessierten als auch Führungskräften 
aller Branchen zu demonstrieren, wie moderne KI-Lösungen autark und datenschutzfreundlich 
umgesetzt werden können.

|

Description
-----------

oVoGPT (`our very own GPT`) is a lightweight demo application that lets you 
run a language model, similar to ChatGPT, directly on your own computer or 
server. No internet connection is required; all data is processed locally 
and never leaves your system.

This demo is designed to show both tech enthusiasts and decision-makers across 
all industries how modern AI solutions can be implemented autonomously and 
with full data privacy.

|

Getting Started
---------------

First download and install Ollama from `here <https://ollama.com/download>`__. 
Then clone this repository and 
run `setup.bat <https://github.com/sinusphi/ovogpt/blob/main/setup.bat>`__ to 
create the virtual environment and install dependencies. 

Start the server 
with `start_server.bat <https://github.com/sinusphi/ovogpt/blob/main/start_server.bat>`__. 
If your browser doesn't open automatically, go to `127.0.0.1:5000` in your 
browser to access the chat page.

Ouput: 

.. code-block:: bash

    Device set to use cpu
    * Serving Flask app 'ovo'
    * Debug mode: off
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    127.0.0.1 - - [26/Jun/2025 13:52:43] "GET / HTTP/1.1" 200 -

|

Contributing
------------

Contributions are welcomed, as well as `Pull
requests <https://github.com/sinusphi/ovogpt/pulls>`__, `bug
reports <https://github.com/sinusphi/ovogpt/issues>`__, and `feature
requests <https://github.com/sinusphi/ovogpt/issues>`__.
