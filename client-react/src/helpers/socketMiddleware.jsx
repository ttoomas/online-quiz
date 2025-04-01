import { useEffect, useRef } from "react";
import { io } from "socket.io-client";
import { useNavigate } from "react-router-dom";
import { SocketContext } from "./socketContext";
import { useDispatch } from "react-redux";
import { setGuessedPlayers, setQuestion, setRoundResults } from "./redux/slice";

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

        socket.on("updateGuessedPlayers", (data) => {
            const guessedPlayers = data.guessed_players;
            dispatch(setGuessedPlayers(guessedPlayers));
        })

        socket.on("showRoundResults", (data) => {
            const roundResults = {
                title: data.title,
                totalQuestionNumber: data.number_of_questions,
                currentQuestionNumber: data.current_question,
                answers: data.round_answers,
                results: data.round_results
            };
            dispatch(setRoundResults(roundResults));
            navigate("/round-results", { replace: true });
        })

        return () => {
            socket.off("navigate");
            socket.off("showQuestion");
            socket.off("updateGuessedPlayers");
            socket.off("showRoundResults");
        }
    }, [navigate]);

    return (
        <SocketContext.Provider value={{ socket: socketRef.current }}>
            {children}
        </SocketContext.Provider>
    );
};

