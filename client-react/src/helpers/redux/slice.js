import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
    name: "user",
    initialState: {
        question: {
            title: "",
            answers: [],
            number_of_questions: 0,
            current_number: 0,
            time: 0,
        },
    },
    reducers: {
        setQuestion: (state, action) => {
            state.question = action.payload; // Update the question state with the payload
        },
    },
});

export const { setQuestion } = userSlice.actions;
export default userSlice.reducer;