import "./Results.css";
import { useNavigate } from 'react-router-dom';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import React from "react";
import { Button } from "primereact/button";
import { FaMedal } from "react-icons/fa";
import { useCookies } from "react-cookie";
import { useSelector } from "react-redux";

export default function Results() {
    const [cookies, setCookie, deleteCookie] = useCookies(["quiz-token"]);    
    const quizResults = useSelector((state) => {
        console.log(state.quiz.quizResults)
        return state.quiz.quizResults;
    });
    
    const navigate = useNavigate();
    const redirectTo = () => {
        deleteCookie("quiz-token");
        
        return navigate('/', { replace: true });
      };
    
    return(
        <>
            {quizResults ? (
                <>
                <div className="results">
                    <h2>You have finished this quiz!</h2>
                    <div>Number of questions: {quizResults.numberOfQuestions}</div>
                    <div>Number of correct answers: {quizResults.correctAnswers}</div>
                    <h4>You were {quizResults.playerPosition} out of {quizResults.totalPlayers} players</h4>
                </div>
                <DataTable className="tabulka2"  value={quizResults.results} tableStyle={{ width: '30%', margin: '0 auto', minWidth: '400px' }}>
                    <Column field="position" header="position" > postio=<FaMedal /></Column>
                    <Column field="username" header="username" ></Column>
                    <Column field="score" header="score" ></Column>
                </DataTable>
                
                <div className="again">
                    <Button className="results_button" onClick={redirectTo} label="Play again" />
                </div>
                </>
            ) : (
                <div>
                    <h1>Loading</h1>
                </div>
            )}
        </>
    )
}