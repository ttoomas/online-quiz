import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { SocketProvider } from "./helpers/socketMiddleware";

import MainPage from './pages/MainPage/MainPage';
import Lobby from './pages/lobby/Lobby';
import Question from './pages/Question/Question';
import Wait from "./pages/wait/Wait";
import Results from "./pages/results/Results";
import Test from "./pages/test/test";
import { CookiesProvider } from "react-cookie";


function App() {
    return (
        <Router>
            <CookiesProvider  defaultSetOptions={{ path: '/' }}>
                <SocketProvider>
                    <Routes>
                        <Route path="/" element={<MainPage />} />
                        <Route path="/lobby" element={<Lobby />} />
                        <Route path="/question" element={<Question />} />
                        <Route path="/wait" element={<Wait />} />
                        <Route path="/results" element={<Results />} />
                        <Route path="/test" element={<Test />} />
                    </Routes>
                </SocketProvider>
            </CookiesProvider>
        </Router>
    )
}

export default App