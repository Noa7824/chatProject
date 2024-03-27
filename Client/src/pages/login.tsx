import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateCurrentUser } from "../redux/users/usersSlice";
import axios from "axios";
import { SERVER_BASE_URL } from "../utils/base_URL";

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [loginError, setLoginError]: any = useState();
    const currentUser = useSelector((store: any) => store.users.currentUser)
    const dispatch = useDispatch()

    const handleLogin = async () => {
        setLoginError(null)
        try {
            const response = await axios.post(`${SERVER_BASE_URL}/login`, { email, password });
            console.log(response.data.user, "response");
            if (response.status === 200) {
                const user = response.data.user;
                dispatch(updateCurrentUser(user))
                // הפניה לדף הבית
            } else if (response.status === 401)
                setLoginError("Email or password is incorrect")
            else setLoginError("Login failed")
        } catch (error) {
            setLoginError("Error: " + error)
        }
    };


    // אפשר להוסיף בדיקות תקינות (אפשר לבקש מצאט)
    return (
        <>
            {currentUser && <> {currentUser.email} : {currentUser._id} </> }
            <input type="text" placeholder="Enter Email" onChange={(e) => setEmail(e.target.value)} /><br />
            <input type="text" placeholder="Password" onChange={(e) => setPassword(e.target.value)} /><br />
            <button onClick={handleLogin}> Login </button><br />
            {loginError && <div style={{ color: "red" }}>{loginError}</div>}
            <button> A new account - Sign up </button>

        </>
    )
}

export { Login };