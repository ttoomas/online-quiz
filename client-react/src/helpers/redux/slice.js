import { createSlice } from "@reduxjs/toolkit";

const quizSlice = createSlice({
    name: "quiz",
    initialState: {
        question: {
            title: "",
            answers: [],
            totalQuestiosNumber: 0,
            currentQuestionNumber: 0,
            time: 0,
        },
        guessedPlayers: [],
        roundResults: {
            title: "",
            totalQuestionNumber: 0,
            currentQuestionNumber: 0,
            answers: [],
            results: [],
        }
    },
    reducers: {
        setQuestion: (state, action) => {
            state.question = action.payload; // Update the question state with the payload
        },
        setGuessedPlayers: (state, action) => {
            state.guessedPlayers = action.payload; // Update the guessed players state with the payload
        },
        setRoundResults: (state, action) => {
            state.roundResults = action.payload; // Update the round results state with the payload
        },
    },
});

export const { setQuestion, setGuessedPlayers, setRoundResults } = quizSlice.actions;
export default quizSlice.reducer;