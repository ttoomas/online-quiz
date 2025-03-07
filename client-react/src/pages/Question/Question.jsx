import { Link } from "react-router-dom";
import "./Question.css";
import { Button } from 'primereact/button';
import React from 'react';
import { useNavigate } from "react-router-dom";


export default function Question() {

    const navigate = useNavigate();

    const redirectTo = () => {
        return navigate(`/wait`, { replace: true });
      };
    
      setTimeout(() => {
        
      }, 1000);

    const data={
        title: "otázka?",
        answers: [
            "jenda", 
            "dva",
            "tri",
            "ctyri"
        ],
        number_of_questions: 25,
        current_number: 10
    }

    const save = () => {
        
        navigate(`/wait`, { replace: true });
    };

    return (
        <div className="otazky">
            <div className="otazka">Otázka: {data.current_number}/{data.number_of_questions}</div>
            <h1>{data.title}</h1>
            <div className="card flex justify-content-center">
                
                {data.answers.map((answer) => {
                    return (
                        <Button className="question_button" label={answer} onClick={save}  />
                    )

                })}
                
            </div>
        </div>
    )
}