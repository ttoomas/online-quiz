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

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
      };
    
      const handlePost = (e) => {
        e.preventDefault();
        postForm();
      };

        useEffect(() => {
            setProducts ([{name: "nick", score: 15 }, {name: "nick", score: 15}, {name: "nick", score: 15}]);
        }, []);

    const redirectTo = () => {
        return navigate(`/lobby`, { replace: true });
      };
    
    return(
        <>
        <div className="results">
            <h2>You have finished this quiz!</h2>
            <div>number of questions: </div>
            <div>number of correct answers: </div>
            <h4>You were "neco" out of "neco" players </h4>
        </div>
        <DataTable className="tabulka2"  value={products} tableStyle={{ width: '30%', margin: '0 auto', minWidth: '400px' }}>
            <Column field="position" header="position" > postio=<FaMedal /></Column>
            <Column field="name" header="nickname" ></Column>
            <Column field="score" header="score" ></Column>
        </DataTable>
        <div className="again">
            <Button className="results_button" onSubmit={handlePost} onClick={redirectTo} label="Play again" />
        </div>
        </>
    )
}