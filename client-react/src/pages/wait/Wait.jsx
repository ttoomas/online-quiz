import { Link } from "react-router-dom"
import "./Wait.css";

import { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Toast } from 'primereact/toast';


export default function Wait() {
    const toast = useRef(null);
    const navigate = useNavigate();

    const redirectTo = () => {
        return navigate(`/question`, { replace: true });
      };
    

    useEffect(() => {
        toast.current.show({ severity: 'success', summary: 'Odesláno!', detail: 'Vaše odpověd byla uložena.' });
        
        
    }, []);

    return(
        <>
        <div className="wait">
            <Toast ref={toast}></Toast>
            <h1>Waiting for other players to answer...</h1>
        </div>
        </>
    )
}