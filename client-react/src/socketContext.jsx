// socketContext.js
import { createContext, useContext, useEffect, useState } from "react";
import { io } from "socket.io-client";
import { useNavigate } from "react-router-dom";

const SocketContext = createContext(null);

export const SocketProvider = ({ children }) => {
  const [socket] = useState(() => io("http://localhost:5000"));
  const [messages, setMessages] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    console.log(socket)
  })

  useEffect(() => {
    socket.on("navigate", (data) => {
        console.log(data)
    //   setMessages((prev) => [...prev, data.message]);
    //   navigate(`/${data.page}`); // Redirect to the page sent from backend
    });

    return () => socket.off("navigate"); // Clean up on unmount
  }, [socket, navigate]);

  return (
    <SocketContext.Provider value={{ socket, messages }}>
      {children}
    </SocketContext.Provider>
  );
};

export const useSocket = () => useContext(SocketContext);
