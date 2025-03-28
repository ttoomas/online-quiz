import "./Question.css";
import { Button } from 'primereact/button';
import React from 'react';
import { useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";


export default function Question() {
    const navigate = useNavigate();
    const question = useSelector((state) => state.user.question);

    const redirectTo = () => {
        return navigate(`/wait`, { replace: true });
    };
    
    const save = () => {
        navigate(`/wait`, { replace: true });
    };

    return (
        <>
        {question ? (
            <div className="otazky">
                <div className="otazka">Otázka: {question.current_question}/{question.number_of_questions}</div>
                <p>Time: {question.time}</p>
                <h1>{question.title}</h1>
                <div className="card flex justify-content-center">
                    {question.answers.map((answer) => {
                        return (
                            <Button className="question_button" label={answer.answer} onClick={save}  />
                        )
                    })}
                </div>
            </div>
        ) : (
            <div>
                <h1>Loading question</h1>
            </div>
        )}
        </>
    )
}