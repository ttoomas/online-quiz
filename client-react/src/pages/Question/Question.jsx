import { Link } from "react-router-dom";
import "./Question.css";
import { Button } from 'primereact/button';
import React, { useEffect } from 'react';
import { useNavigate } from "react-router-dom";

export default function Question() {
    const navigate = useNavigate();

    useEffect(() => {
        document.body.style.backgroundColor = "rgb(239, 248, 253)"; // Nastavení barvy pozadí

        return () => {
            document.body.style.backgroundColor = ""; // Reset při opuštění stránky
        };
    }, []);

    const save = () => {
        navigate(`/wait`, { replace: true });
    };

    const data = {
        title: "otázka?",
        answers: ["jenda", "dva", "tri", "ctyri"],
        number_of_questions: 25,
        current_number: 10
    };

    return (
        <div className="otazky">
            <div className="otazka">Otázka: {data.current_number}/{data.number_of_questions}</div>
            <h1>{data.title}</h1>
            <div className="card flex justify-content-center">
                {data.answers.map((answer, index) => (
                    <Button key={index} className="question_button" label={answer} onClick={save} />
                ))}
            </div>
        </div>
    );
}