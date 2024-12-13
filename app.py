import chainlit as cl
from chainlit.cli import cli
from src.llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    #our logic should mention here
    # Send a response back to the user
    await cl.Message(
        content=f"Received : {message.content}",
    ).send()
