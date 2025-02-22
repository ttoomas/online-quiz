import React, { useState, useEffect } from 'react';
import { socket } from './socket';

export default function App() {
  const [isConnected, setIsConnected] = useState(socket.connected);
  const [fooEvents, setFooEvents] = useState([]);

  useEffect(() => {
    function onConnect() {
      console.log("Connection");
      
      setIsConnected(true);
    }

    function onDisconnect() {
      setIsConnected(false);
    }

    function onFooEvent(value) {
      setFooEvents(previous => [...previous, value]);
    }

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);
    socket.on('foo', onFooEvent);

    return () => {
      socket.off('connect', onConnect);
      socket.off('disconnect', onDisconnect);
      socket.off('foo', onFooEvent);
    };
  }, []);

  function sendTestEvent(){
    const roomId = "kareljaromir123id"
    const userName = "karel"
    socket.emit('connectToRoom', {
      roomId: roomId,
      userName: userName
    });
  }

  return (
    <div className="App">
      <h1>Socket.IO Test</h1>
      <button onClick={sendTestEvent}>Click to join a room with some random id</button>
    </div>
  );
}