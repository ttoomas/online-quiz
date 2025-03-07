import { Link, useNavigate } from "react-router-dom";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import "./MainPage.css";
import { useState } from "react";

export default function MainPage() {
  const [formData, setFormData] = useState();
  const navigate = useNavigate();
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handlePost = (e) => {
    e.preventDefault();
    postForm();
  };

  const redirectTo = () => {
    return navigate(`/lobby`, { replace: true });
  };

  return (
    <>
      <div className="uvodnistranka">
        <h1>Online-quiz</h1>

        <div>
          <h3>Zadejte token:</h3>
          <InputText 
            name="token"
            placeholder="token"
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
        </div>
        <div className="enter">
          <Button className="button_main" onSubmit={handlePost} onClick={redirectTo} label="Enter" />
        </div>
      </div>
    </>
  );
}
