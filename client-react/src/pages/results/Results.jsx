import "./Results.css";
import { useNavigate } from 'react-router-dom';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import React from "react";
import { Button } from "primereact/button";
import { FaMedal } from "react-icons/fa";
import { useCookies } from "react-cookie";

export default function Results() {
    const [cookies, setCookie, deleteCookie] = useCookies(["quiz-token"]);    

    const data = {
        numberOfQuestions: 10,
        correctAnswers: 5,
        totalPlayers: 10,
        playerPosition: 5,
        results: [
            {
                position: 1,
                username: "nick",
                score: 15
            },
            {
                position: 2,
                username: "nick",
                score: 15
            }
        ]
    }
    
    const navigate = useNavigate();
    const redirectTo = () => {
        deleteCookie("quiz-token");
        
        return navigate('/', { replace: true });
      };
    
    return(
        <>
            <div className="results">
                <h2>You have finished this quiz!</h2>
                <div>Number of questions: {data.numberOfQuestions}</div>
                <div>Number of correct answers: {data.correctAnswers}</div>
                <h4>You were {data.playerPosition} out of {data.totalPlayers} players</h4>
            </div>
            <DataTable className="tabulka2"  value={data.results} tableStyle={{ width: '30%', margin: '0 auto', minWidth: '400px' }}>
                <Column field="position" header="position" > postio=<FaMedal /></Column>
                <Column field="username" header="username" ></Column>
                <Column field="score" header="score" ></Column>
            </DataTable>
            
            <div className="again">
                <Button className="results_button" onClick={redirectTo} label="Play again" />
            </div>
        </>
    )
}