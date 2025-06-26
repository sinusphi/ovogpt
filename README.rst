oVoGPT
******

**Das eigene, lokale und sichere Sprachmodell.**

.. image:: https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=FFE873
    :target: https://www.python.org/downloads

.. image:: https://img.shields.io/badge/code%20style-black-000000
    :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/donations-paypal-pink
    :target: https://paypal.me/yserestou

|

Beschreibung
------------

oVoGPT (Our Very Own GPT) ist eine leichtgewichtige Demo-Anwendung, mit der sich ein Sprachmodell, ähnlich wie ChatGPT, direkt auf dem eigenen Computer oder Server betreiben lässt. Eine Internetverbindung ist nicht erforderlich, sämtliche Daten werden lokal verarbeitet und verlassen das System zu keinem Zeitpunkt.
oVoGPT möchte sowohl Technik-Interessierten als auch Führungskräften aller Branchen, wie moderne KI-Lösungen autark und datenschutzfreundlich umgesetzt werden können.

|

Description
-----------

oVoGPT (`our very own GPT`) is a lightweight demo application that lets you run a language model, similar to ChatGPT, directly on your own computer or server. No internet connection is required; all data is processed locally and never leaves your system.
oVoGPT is designed to show both tech enthusiasts and decision-makers across all industries how modern AI solutions can be implemented autonomously and with full data privacy.

|

Run oVo
-------

First launch a console. Create and activate a virtual environment:

.. code-block:: bash

    $ python -m venv <your_venv>
    $ source <your_venv>/Scripts/activate

|

Clone this repository and install the `requirements <https://github.com/sinusphi/ovogpt/requirements.txt>`__.

|

Start the server:

.. code-block:: bash

    $ python ovogpt/ovogpt/ovo.py
    Device set to use cpu
    * Serving Flask app 'ovo'
    * Debug mode: off
    WARNING: 
    This is a development server. 
    Do not use it in a production deployment. 
    Use a production WSGI server instead.
    * Running on all addresses (0.0.0.0)
    * Running on http://127.0.0.1:5000
    * Running on http://___.___.___.__:5000
    Press CTRL+C to quit
    127.0.0.1 - - [26/Jun/2025 13:52:43] "GET / HTTP/1.1" 200 -

|

Then open `127.0.0.1:5000` in your browser to access the chat page.

|

Contributing
------------

Contributions are welcomed, as well as `Pull
requests <https://github.com/sinusphi/ovogpt/pulls>`__, `bug
reports <https://github.com/sinusphi/ovogpt/issues>`__, and `feature
requests <https://github.com/sinusphi/ovogpt/issues>`__.
