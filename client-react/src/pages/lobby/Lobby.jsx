import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Link } from "react-router-dom";
import "./Lobby.css";
import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSocket } from '../../helpers/socketContext';

export default function Lobby() {
    const [players, setPlayers] = useState([]);
    const navigate = useNavigate();

    const redirectTo = () => {
        return navigate(`/question`, { replace: true });
    };

    
    // Socket
    const { socket } = useSocket();
    
    socket.on("updateRoomPlayers", (data) => {
        const playerNames = data.playerNames.map(value => { return { name: value }});
        setPlayers(playerNames);
    })

    function getRoomPlayers(){
        socket.emit("getRoomPlayers", (data) => {
            const playerNames = data.playerNames.map(value => { return { name: value }});
            setPlayers(playerNames);
        });
    }

    useEffect(getRoomPlayers, []);


    return(
        <>
        <div className="lobby">
            <h1>Waiting for other players...</h1>
            <DataTable
                className="tabulka"
                emptyMessage="Zatím žádný hráč není připojen"
                value={players}
                tableStyle={{ width: '40%', margin: '0 auto', minWidth: '500px' }}
            >
                <Column field="name" header="members" ></Column>
            </DataTable>
        </div>
        </>
    )
}