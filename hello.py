import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv() 

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

MODEL = "claude-haiku-4-5"

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude"
        }
    ],
    model=MODEL,
)

for block in message.content:
    if block.type == "text":
        print(block.text)