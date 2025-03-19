import React, { useState } from 'react'
import { useSocket } from '../../helpers/socketContext';

function test() {
    const [formData, setFormData] = useState();
    
    const { socket } = useSocket();
    
    function submit(){
        console.log(formData);
        
        socket.emit("createRoom", formData)
    }
    
    return (
        <div>
            <input type="text" onChange={(e) => {setFormData({key: e.target.value})}} />
            <button onClick={submit}>Submit</button>
        </div>
    )
}

export default test