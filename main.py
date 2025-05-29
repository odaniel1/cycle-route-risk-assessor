from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from services.strava_client import extract_route_id
import re

app = Flask(__name__)


@app.route("/whatsapp", methods=['GET', 'POST'])
def whatsapp_reply():
    """Respond to incoming WhatsApp messages, if the include a Strava route URL."""
    incoming = request.values.get('Body', '')
    
    # Check if the incoming message contains a Strava route ID
    route_id = extract_route_id(incoming)

    if route_id:
        resp = MessagingResponse()
        resp.message(f"You sent Strava route: {route_id}")
        return str(resp)
    
    return('',204)


if __name__ == "__main__":
    app.run(debug=True)
