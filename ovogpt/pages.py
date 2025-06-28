"""HTML Pages"""
chat_page = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>oVoGPT</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 40px 20px;
            background: #121212;
            color: #f0f0f0;
        }

        .container {
            max-width: 600px;
            margin: auto;
            background: #1e1e1e;
            border-radius: 12px;
            box-shadow: 0 0 15px #00bcd4;
            padding: 24px;
        }

        h1 {
            font-size: 2em;
            text-align: center;
            margin-bottom: 10px;
        }

        .logo {
            display: block;
            margin: 0 auto 20px auto;
            width: 100px;
            filter: drop-shadow(0 0 10px #00bcd4);
        }

        textarea {
            width: 100%;
            min-height: 60px;
            border-radius: 8px;
            border: 1px solid #555;
            background: #2c2c2c;
            color: #f0f0f0;
            padding: 10px;
        }

        button {
            padding: 8px 18px;
            font-size: 1em;
            border-radius: 8px;
            background: #00bcd4;
            color: #000;
            border: none;
            cursor: pointer;
            margin-top: 10px;
        }

        .answer {
            margin-top: 20px;
            background: #2a2a2a;
            border-radius: 8px;
            padding: 12px;
            border: 1px solid #00bcd4;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="/static/icon1.png" alt="Logo" class="logo">
        <h1>oVoGPT</h1>
        <form method="POST">
            <label for="frage">Ask oVoGPT:</label><br>
            <textarea name="frage" id="frage">{{ frage or '' }}</textarea><br>
            <button type="submit">Send</button>
        </form>
        {% if antwort %}
        <div class="answer">
            <strong>Response:</strong><br>
            {{ antwort }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""
