import base64
import random
import string
from datetime import datetime

def encode_secret(message):
    encoded = base64.b64encode(message.encode()).decode()
    return f"[ENCODED] {encoded}"

def decode_secret(encoded):
    try:
        decoded = base64.b64decode(encoded.encode()).decode()
        return f"[DECODED] {decoded}"
    except Exception:
        return "[ERROR] Could not decode."

def random_key(length=16):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def fortune():
    fortunes = [
        "The shadows hide the truth.",
        "Keys are everywhere if you know where to look.",
        "Noise often hides the signal.",
        "Time decays all secrets.",
        "Even encrypted hearts can be broken."
    ]
    return random.choice(fortunes)

if __name__ == "__main__":
    msg = "Trust no one."
    encoded = encode_secret(msg)
    print(encoded)
    print(decode_secret(encoded.split(" ")[1]))

    key = random_key()
    print(f"Generated Key: {key}")

    print("Fortune:", fortune())
    print("Timestamp:", datetime.now().isoformat())
