import { socket } from "./init";

function joinRoom({
    roomId,
    userName
}){
    console.log('Joining room', roomId);

    socket.emit('connectToRoom', {
        roomId: roomId,
        userName: userName
    });
}

export {
    joinRoom
}