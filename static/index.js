"use strict";
var socket = io();
        socket.on('connect', function() {
            socket.emit('my event', {data: 'I\'m connected!'});
        });

//const websocket = new WebSocket("ws://localhost:8001/");

const $BUTTON = $("#test-form-button");
const $FORM_INPUT = $("#text-to-send");
const $INCOMING = $("#recieved");

$BUTTON.on("click", sendMessage);
function sendMessage(evt){
    evt.preventDefault();
    // websocket.send($FORM_INPUT.val());
    socket.emit("message",$FORM_INPUT.val());
    socket.emit("test", "some other data here");
}

//websocket.addEventListener("message", recieveMessage)
socket.on("message received", recieveMessage)
function recieveMessage(message){
    console.log(message);
    $INCOMING.append(`<p>${message}</p>`)
}