import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import MainPage from './pages/MainPage/MainPage'
import Layout from "./Layout";

function App() {

  return (
    <>
     <Router>
            <Layout>
                <Routes>
                    <Route path="/" element={<MainPage />} />

                   
            
                </Routes>
            </Layout>
        </Router>
    </>
  )
}

export default App
