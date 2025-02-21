import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Link } from "react-router-dom";
import "./Lobby.css";
import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Lobby() {

    const [products, setProducts] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        setProducts ([{name: "nick"}, {name: "nick"}, {name: "nick"}, {name: "nick"}]);
    }, []);

    const redirectTo = () => {
        return navigate(`/question`, { replace: true });
      };
    
      setTimeout(() => {
        navigate(`/question`, { replace: true });
      }, 2000);

    return(
        <>
        <div className="lobby">
            <h1>Waiting for other players...</h1>
            <DataTable className="tabulka"  value={products} tableStyle={{ minWidth: '50rem' }}>
                <Column field="name" ></Column>
            </DataTable>
        </div>
        </>
    )
}