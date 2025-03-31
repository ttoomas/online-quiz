import "./Question.css";
import { Button } from 'primereact/button';
import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { useSocket } from "../../helpers/socketContext";


export default function Question() {
    const navigate = useNavigate();
    const question = useSelector((state) => {
        return state.quiz.question;
    });
    const [timeLeft, setTimeLeft] = useState(0);
    const { socket } = useSocket();

    const handlePost = async (answerId) => {
        await sendAnswer(answerId);
        navigate(`/wait`, { replace: true });
    };

    // Socket
    async function sendAnswer(answerId){
        return new Promise((resolve, reject) => {
            socket.emit("sendAnswer", {
                answer_id: answerId
            }, handleResponse);

            function handleResponse(rsp){
                resolve(rsp);
            }
        })
    }
    
    // Question Countdown
    useEffect(() => {
        setTimeLeft(question.time);
        let localTimeLeft = question.time;

        const interval = setInterval(() => {
            if (localTimeLeft > 0) {
                localTimeLeft--;
                setTimeLeft(localTimeLeft);
                return;
            }

            clearInterval(interval);
        }, 1000);        

        return () => {
            clearInterval(interval);
        }
    }, [question.time])

    return (
        <>
        {question ? (
            <div className="otazky">
                <div className="otazka">Otázka: {question.currentQuestionNumber}/{question.totalQuestiosNumber}</div>
                <p>Time: {timeLeft}</p>
                <h1>{question.title}</h1>
                <div className="card flex justify-content-center">
                    {question.answers.map((answer) => {
                        return (
                            <Button key={answer.answer_id} className="question_button" label={answer.answer} onClick={() => handlePost(answer.answer_id)}  />
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