from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['GET', 'POST'])
def whatsapp_reply():
    """Respond to incoming WhatsApp messages."""
    incoming = request.values.get('Body', '')
    
    resp = MessagingResponse()

    # Simple echo bot
    resp.message(f"You said: {incoming}")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)