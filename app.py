from flask import Flask, request, render_template, jsonify, session
# import asyncio
# import websockets

from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
app.config["SECRET_KEY"] = "this-is-secret"



@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('message')
def receive_msg(message):
    print(message)
    emit('message received', f"{message} message received");

@socketio.on('test')
def receive_test(test):
    print(test)
    emit('message received', f"{test} message received");


# @socketio.on("score")


if __name__ == '__main__':
    socketio.run(app)

# async def handler(websocket):
#     while True:
#         try:
#             message = await websocket.recv()
#         except websockets.ConnectionClosedOK:
#             print("connection closed")
#             break
#         print(message)
#         await websocket.send(f"{message} message recieved")

# #coroutine that manages a connection (handler)
# #listener for where the server can be reached
# #
# async def main():
#     async with websockets.serve(handler, "", 8001):
#         print("connection established")
#         await asyncio.Future()  # run forever
#         print("after future")


# # if __name__ == "__main__":
# #     asyncio.run(main())

# @app.get("/")
# def homepage():
#     """Shows the homepage"""
#     asyncio.run(main())


#     return render_template("index.html")