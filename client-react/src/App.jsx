import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import MainPage from './pages/MainPage/MainPage';
import Lobby from './pages/lobby/Lobby';
import Question from './pages/Question/Question';
import Layout from "./Layout";
import Wait from "./pages/wait/Wait";
import Results from "./pages/results/Results";

function App() {

  return (
    <>
     <Router>
            <Layout>
                <Routes>
                    <Route path="/" element={<MainPage />} />
                </Routes>
                <Routes>
                    <Route path="/lobby" element={<Lobby />} />
                </Routes>
                <Routes>
                    <Route path="/question" element={<Question />} />
                </Routes>
                <Routes>
                    <Route path="/wait" element={<Wait />} />
                </Routes>
                <Routes>
                    <Route path="/results" element={<Results />} />
                </Routes>

            </Layout>
        </Router>
    </>
  )
}

export default App
