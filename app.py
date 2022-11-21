from flask import Flask, request, render_template, jsonify, session
import asyncio
import websockets

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())