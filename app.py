from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("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"))

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Nova AI</title></head>
        <body style="font-family: Arial; text-align:center; margin-top:100px;">
            <h1>Nova AI Assistant</h1>
            <form action="/chat" method="post">
                <input name="user_input" placeholder="Ask me anything..." style="width:300px; padding:10px;">
                <button type="submit">Send</button>
            </form>
        </body>
    </html>
    '''

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        ai_message = response.choices[0].message.content
    except Exception as e:
        ai_message = f"Error: {str(e)}"

    return jsonify({"response": ai_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
