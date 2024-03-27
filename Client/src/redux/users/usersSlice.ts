import { createSlice, current } from "@reduxjs/toolkit";

const initialState = {
    currentUser: null
}

const usersSlice = createSlice({
    name: "users",
    initialState,
    reducers: {
        updateCurrentUser: (state, action) => {
            state.currentUser = action.payload
        }
    }
})

export const { updateCurrentUser } = usersSlice.actions;

export default usersSlice.reducer
