import { useSelector } from "react-redux";
import "./RoundResults.css";

export default function RoundResults() {
    const roundResults = useSelector((state) => {
        console.log(state.quiz.roundResults)
        return state.quiz.roundResults;
    });

    return (
        <>
        {roundResults ? (
            <div className="otazky">
                <div className="otazka">Otázka: {roundResults.currentQuestionNumber}/{roundResults.totalQuestionNumber}</div>
                <h1>{roundResults.title}</h1>
                <div className="card flex justify-content-center">
                    {roundResults.answers.map((answer) => (
                        <p key={answer.answer_id} className={
                            "answer " + (
                                answer.is_correct == true ? "correct" : (
                                    answer.is_correct == false ? "incorrect" : ""
                                ))
                        }>{answer.answer}</p>
                    ))}
                </div>

                <h2 className="roundResults__title">Výsledky hráčů:</h2>
                <div className="roundResults__players">
                    {roundResults.results.map((player) => (
                        <div key={player.username} className="roundResults__player">
                            <p className={"roundResults__player " + (player.is_correct ? "correct" : "incorrect")}>{player.username}: {player.score}</p>
                        </div>
                    ))}
                </div>
            </div>
        ) : (
            <div>
                <h1>Loading Round Results</h1>
            </div>
        )}
        </>
    )
}