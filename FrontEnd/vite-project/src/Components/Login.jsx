import React, {useState} from "react";
import "../Styles/login.css"
const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    // cosnt [errorMessage, setErrorMessage] = useState('');

    const handleSubmit = (e) => {
        return 1;
    }


return (
    <div className="Login-container">
        <div className="Instituiton-div">
            <div className="Institution-div-first-innerdiv">
                <div>Monday</div>
                <div>6:50AM</div>
                <div>15th Aug, 2024</div>
            </div>
            <div className="Institution-div-second-innerdiv">
                 <img src="/src/assets/logo.svg" alt="your logo here" />
            </div>
            <div className="Institution-div-third-innerdiv">
                 <h1>EECOHM COLLEGE</h1>
                 <p>Birtamode-1, Jhapa</p>
            </div>
            <div className="Institution-div-forth-innerdiv">
                <div>023-546392</div>
                <div>eecohm@gmail.com</div>
            </div>
        </div>
        <div className="Login-div">
        <div className="login-div-first-innerdiv">
                 <img src="/src/assets/icons/user_icon.svg" alt="user icon here" />
            </div>
        <div className="login-form-div">
            {/* <h3>enter your email and password</h3> */}
            <form onSubmit={handleSubmit}>
                <label htmlFor="email">Email:</label>
                <input name="email" type="email" placeholder="example@gmail.com" />
                <label htmlFor="password">Password:</label>
                <input name="password" placeholder="password" type="password" />
                <button>Login</button>
            </form>
            <a href="#">Forgot Password?</a>
        </div>
        </div>
    </div>
    
);
}

export default Login;