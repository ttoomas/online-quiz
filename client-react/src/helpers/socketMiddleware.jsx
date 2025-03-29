import { useEffect, useRef } from "react";
import { io } from "socket.io-client";
import { useNavigate } from "react-router-dom";
import { SocketContext } from "./socketContext";
import { useDispatch } from "react-redux";
import { setQuestion } from "./redux/slice";

export const SocketProvider = ({ children }) => {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const socketRef = useRef();

    if (!socketRef.current) {
        socketRef.current = io("http://localhost:5100");

        socketRef.current.emit("initClient", {
            "role": "player"
        })
    }

    useEffect(() => {
        const socket = socketRef.current;

        console.log(socket);
        
        socket.on("navigate", (data) => {
            console.log(data);
        });

        socket.on("showQuestion", (data) => {
            const newData = {
                title: data.title,
                answers: data.answers_list,
                totalQuestiosNumber: data.number_of_questions,
                currentQuestionNumber: data.current_question,
                time: data.time                
            }
            dispatch(setQuestion(newData));

            navigate("/question", { replace: true });
        });

        return () => socket.off("navigate");
    }, [navigate]);

    return (
        <SocketContext.Provider value={{ socket: socketRef.current }}>
            {children}
        </SocketContext.Provider>
    );
};

