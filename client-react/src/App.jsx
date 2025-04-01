import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { CookiesProvider } from "react-cookie";
import { SocketProvider } from "./helpers/socketMiddleware";
import GlobalWrapper from "./helpers/GlobalWrapper";

import MainPage from './pages/MainPage/MainPage';
import Lobby from './pages/lobby/Lobby';
import Question from './pages/Question/Question';
import Wait from "./pages/wait/Wait";
import RoundResults from "./pages/RoundResults/RoundResults";
import Results from "./pages/results/Results";


function App() {
    return (
        <Router>
            <CookiesProvider  defaultSetOptions={{ path: '/' }}>
                <SocketProvider>
                    <GlobalWrapper>
                        <Routes>
                            <Route path="/" element={<MainPage />} />
                            <Route path="/lobby" element={<Lobby />} />
                            <Route path="/question" element={<Question />} />
                            <Route path="/wait" element={<Wait />} />
                            <Route path="/round-results" element={<RoundResults />} />
                            <Route path="/results" element={<Results />} />
                        </Routes>
                    </GlobalWrapper>
                </SocketProvider>
            </CookiesProvider>
        </Router>
    )
}

export default App