import { useEffect, useState } from 'react';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import { useSocket } from './socketContext';

const PageStatuses = {
    waiting: "/lobby"
}

const GlobalWrapper = ({ children }) => {
    const [cookies, setCookie, deleteCookie] = useCookies(["quiz-token"]);
    const { socket } = useSocket();
    const navigate = useNavigate();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        handlePageLoad();
    }, []);

    async function handlePageLoad() {
        const jwtToken = cookies["quiz-token"];

        if (!jwtToken) {
            navigate("/", { replace: true });
            deleteCookie("quiz-token");
            setLoading(false);
            return;
        }

        const result = await checkToken(jwtToken["token"]);

        if (!result.success) {
            navigate("/", { replace: true });
            deleteCookie("quiz-token");
            setLoading(false);
            return;
        }

        navigate(PageStatuses[result.status], { replace: true });
        setLoading(false);
    }

    async function checkToken(jwtToken) {
        return new Promise((resolve, reject) => {
            socket.emit("checkJwtToken", {
                jwtToken: jwtToken
            }, handleResponse)

            function handleResponse(rsp) {
                resolve(rsp);
            }
        })
    }

    if (loading) {
        return <div>Loading...</div>;
    }

    return children;
};

export default GlobalWrapper;