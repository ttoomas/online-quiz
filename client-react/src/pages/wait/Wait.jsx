import { Link } from "react-router-dom"
import "./Wait.css";

import { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Toast } from 'primereact/toast';
import { useSelector } from "react-redux";


export default function Wait() {
    const toast = useRef(null);
    const navigate = useNavigate();
    const userList = useSelector((state) => state.quiz.guessedPlayers);

    const redirectTo = () => {
        return navigate(`/question`, { replace: true });
    
    useEffect(() => {
    document.body.style.backgroundColor = "rgb(239, 248, 253)"; // Nastavení barvy pozadí

    return () => {
        document.body.style.backgroundColor = ""; // Reset při opuštění stránky
    };
}, []);

    useEffect(() => {
        toast.current.show({ severity: 'success', summary: 'Odesláno!', detail: 'Vaše odpověd byla uložena.' });
    }, []);


    return(
        <>
        <div className="wait">
            <Toast ref={toast}></Toast>
            <h1>Waiting for other players to answer...</h1>

            <h2>Players who already guessed:</h2>
            <div>
                {userList.map(player => (
                    <div key={player} className="player">
                        <p>{player}</p>
                    </div>
                ))}
            </div>
        </div>
        </>
    )
}