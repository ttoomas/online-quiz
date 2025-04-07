import { Link, useNavigate } from "react-router-dom";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import "./MainPage.css";
import { useEffect, useState } from "react";
import { useSocket } from "../../helpers/socketContext";
import { useCookies } from "react-cookie";

export default function MainPage() {
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

    const handlePost = async (e) => {
        e.preventDefault();
        
        if (formData["username"].length <= 2 || formData["roomId"].length <= 4 ) {
            setIsError("*zadal jsi špatné údaje")
            return;
        }
        // Validate data
        // Join socket room and redirect
        const result = await joinRoomSocket();

        if(!result.success){
            setIsError("*zadal jsi špatný token")
            
            return;
        }
        else if(!result.jwt){
            throw new Error("JWT token is missing");
        }

        // Set cookie
        setCookie("quiz-token", {
            token: result.jwt
        });
        
        redirectTo();
    };

    const redirectTo = () => {
        return navigate(`/lobby`, { replace: true });
    };

    // Socket
    function initLoadSocket(){

    }

    async function joinRoomSocket(){
        return new Promise((resolve, reject) => {
            socket.emit("joinRoom", {
                roomId: formData.roomId,
                username: formData.username
            }, handleResponse)
    
            function handleResponse(rsp){
                console.log(rsp);
                resolve(rsp);
            }
        })
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
