import os

from dotenv import load_dotenv

def load_config():
    if os.path.exists(
        ".env"
    ):  # this makes it so .env files override whatever other env vars have been loaded in
        load_dotenv(".env", override=True)

    config = {
        "MOLLIE_API_KEY": os.getenv("MOLLIE_API_KEY"),
        "WHISPER_API_KEY": os.getenv("WHISPER_API_KEY"),
    }

    # Validate required settings
    if not config["MOLLIE_API_KEY"]:
        raise ValueError("MOLLIE_API_KEY is not set")

    return config

config = load_config()
