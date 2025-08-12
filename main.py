import chainlit as cl           #Importing chainlit library...

@cl.on_message

async def main(message: cl.Message):
    response = f"Received : {message.content}"
    await cl.Message(content = response).send()