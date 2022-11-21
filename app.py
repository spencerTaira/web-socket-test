from flask import Flask, request, render_template, jsonify, session
import asyncio
import websockets

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            print("connection closed")
            break
        print(message)
        await websocket.send(f"{message} message recieved")

#coroutine that manages a connection (handler)
#listener for where the server can be reached
#
async def main():
    async with websockets.serve(handler, "", 8001):
        print("connection established")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())

@app.get("/")
def homepage():
    """Shows the homepage"""
    asyncio.run(main())


    return render_template("index.html")