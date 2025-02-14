import { Link } from "react-router-dom";
import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';
import "./MainPage.css";
        
const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
};

export default function MainPage() {

    return(
        <>
        <div className="uvodnistranka">
            <h1>Online-quiz</h1>
                <div>
                    <h3>Zadejte token:</h3>
                        <InputText keyfilter="int" placeholder="token" onChange={(e) => handleChange(e)}/>
                </div>
                <div>
                    <h3>Zadejte přezdívku:</h3>
                        <InputText keyfilter="int" placeholder="přezdívka" onChange={(e) => handleChange(e)}/>
                </div>
            <div className="enter"><Button label="Enter" /></div>
        </div>
        </>
    )
}