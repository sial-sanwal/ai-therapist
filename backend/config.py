import os
from dotenv import load_dotenv


load_dotenv()

twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM_NUMBER")
emergency_number = os.getenv("EMERGENCY_CONTACT")
groq_key = os.getenv("GROQ_API_KEY")

