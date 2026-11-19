from dotenv import load_dotenv
import os

load_dotenv()

print("API key loaded:", bool(os.getenv("GOOGLE_API_KEY")))