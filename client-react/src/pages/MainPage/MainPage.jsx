import { Link, useNavigate } from "react-router-dom";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import "./MainPage.css";
import { useEffect, useState } from "react";
import { useSocket } from "../../helpers/socketContext";
import { useCookies } from "react-cookie";

export default function MainPage() {
    // TODO! - on every connect, send token to server and check room id, if it exists, join room
    const [cookies, setCookie] = useCookies(["token"]);
    const { socket } = useSocket();
    
    const [IsError, setIsError,] = useState();
    const [formData, setFormData] = useState();
    const navigate = useNavigate();
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };
    

     useEffect(() => {
            document.body.style.backgroundColor = "rgb(255, 243, 251)"; // Nastavení barvy pozadí
    
            return () => {
                document.body.style.backgroundColor = ""; // Reset při opuštění stránky
            };
        }, []);

    const handlePost = (e) => {
        e.preventDefault();
        
        if (formData["username"].length <= 2 || formData["roomId"].length <= 4 ) {
            setIsError("*zadal jsi špatné údaje")
            return;
        }
        // Validate data
        // TODO: pokud token je mene nez 4 znaky a prezdivka mene nez 2, hodi to error

        // Join socket room and redirect
        const result = {
            success: true
        };

        if(!result.success){
            setIsError("*zadal jsi špatný token")
            
            // TODO: pokud je token spatny, hodi to error
            
            return;
        }
        // else if(!result.jwt){
        //     throw new Error("JWT token is missing");
        // }

        // // Set cookie
        // setCookie("quiz-token", {
        //     token: result.jwt
        // });
        
        redirectTo();
    };

    const redirectTo = () => {
        return navigate(`/lobby`, { replace: true });
    };

    // Socket
    function initLoadSocket(){

    }

    function joinRoomSocket(){
        socket.emit("joinRoom", {
            roomId: formData.roomId,
            username: formData.username
        }, handleResponse)

        function handleResponse(rsp){
            if(!rsp.success){
                // TODO: zobrazit spatny token

                return;
            }

            redirectTo();
        }
    }

    useEffect(initLoadSocket, []);


    return (
        <>
        <div className="uvodnistranka">
            <h1>Online-quiz</h1>

            <div>
            <h3>Zadejte token:</h3>
            <InputText 
                name="roomId"
                placeholder="Room ID"
                onChange={(e) => handleChange(e)}
            />
            </div>
            <div>
            <h3>Zadejte přezdívku:</h3>
            <InputText
                name="username"
                placeholder="přezdívka"
                onChange={(e) => handleChange(e)}
            />
            
                {IsError &&
                  <div className="wrong">{IsError}</div>
                }
            </div>
            <div className="enter">
            <Button className="button_main" onClick={handlePost} label="Enter" />
            </div>
        </div>
        </>
    );
}
