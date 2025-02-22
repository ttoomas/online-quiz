import { socket } from "./init";

function events(){
    // Default
    socket.on('connect', connect);
    socket.on('disconnect', disconnect);
    socket.on('playerWaitingRoom', playerWaitingRoom);

    // Off socket events
    return () => {
        socket.off('connect', connect);
        socket.off('disconnect', disconnect);
        socket.off('playerWaitingRoom', playerWaitingRoom);
    }
}

function connect(){
    console.log("Client connected to server");
    socket.emit("playerInit");
}

function disconnect(){
    console.log("Client disconnected from server");
}

function playerWaitingRoom(){
    console.log("Player is in waiting room");
}

export {
    events
}