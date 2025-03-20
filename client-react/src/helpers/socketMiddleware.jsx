import { useEffect, useRef } from "react";
import { io } from "socket.io-client";
import { useNavigate } from "react-router-dom";
import { SocketContext } from "./socketContext";

export const SocketProvider = ({ children }) => {
    const navigate = useNavigate();
    const socketRef = useRef();

    if (!socketRef.current) {
        socketRef.current = io("http://localhost:5100");
    }

    useEffect(() => {
        const socket = socketRef.current;

        console.log(socket);
        
        socket.on("navigate", (data) => {
            console.log(data);
        });

        return () => socket.off("navigate");
    }, [navigate]);

    return (
        <SocketContext.Provider value={{ socket: socketRef.current }}>
            {children}
        </SocketContext.Provider>
    );
};

