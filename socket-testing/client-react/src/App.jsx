import { useEffect, useState } from "react"
import { events } from "./socket/events";
import { joinRoom } from "./socket/joinRoom";

function App() {
    const [roomId, setRoomId] = useState('');
    const userName = 'karel';

    function handleChange(e){
        setRoomId(e.target.value);
    }

    function handleJoin(){
        joinRoom({
            roomId,
            userName
        });
    }

    // Call the events
    useEffect(events, []);
    
    return (
        <div className="App">
            <h1>Socket.IO Test</h1>
            <input type="text" placeholder='id' onChange={handleChange} />
            <button onClick={handleJoin}>Join room</button>
        </div>
    )
}

export default App