import { Link } from "react-router-dom"
import "./Results.css";
import { useNavigate } from 'react-router-dom';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import { Button } from "primereact/button";
import { FaMedal } from "react-icons/fa";



export default function Results() {
    const navigate = useNavigate();
    const [products, setProducts] = useState([]);

    const data={
        number_of_questions: 25,
        number_of_correct_answers: 11,
        number_of_players: 15,
        finish_position: 13
    }

    useEffect(() => {
        document.body.style.backgroundColor = "rgb(245, 255, 247)"; // Nastavení barvy pozadí

        return () => {
            document.body.style.backgroundColor = ""; // Reset při opuštění stránky
        };
    }, []);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
      };
    
      const handlePost = (e) => {
        e.preventDefault();
        postForm();
      };

        useEffect(() => {
            setProducts ([{position: "1.", name: "nick", score: 15 }, {position: "2.", name: "nick", score: 15}, {position: "3.", name: "nick", score: 15}]);
        }, []);

    const redirectTo = () => {
        return navigate(`/lobby`, { replace: true });
      };
    
    return(
        <>
        <div className="results">
            <h2>You have finished this quiz!</h2>
            <div>number of questions: {data.number_of_questions} </div>
            <div>number of correct answers: {data.number_of_correct_answers}</div>
            <h4>You were {data.finish_position} out of {data.number_of_players} players </h4>
        </div>
        <DataTable className="tabulka2"  value={products} tableStyle={{ width: '160px', margin: '0 auto', minWidth: '600px' }}>
            <Column style={{width: '160px'}} field="position" header="position" > postio=<FaMedal /></Column>
            <Column style={{width: '160px'}} field="name" header="nickname" ></Column>
            <Column style={{width: '160px'}} field="score" header="score" ></Column>
        </DataTable>
        <div className="again">
            <Button className="results_button" onSubmit={handlePost} onClick={redirectTo} label="Play again" />
        </div>
        </>
    )
}