import React, { useState, useContext} from 'react';
import { Link, useHistory } from 'react-router-dom';
import '../styles/Login.css';
import axios from 'axios';
import AppContext from '../context/AppContext';

const URL = "/login";

const Login = () => {
    const [user, setUser] = useState({ email: "", password: "" });
    const { login, setLogin } = useContext(AppContext);
    let history = useHistory();

    function handleChange(event) {
        setUser({
            ...user,
            [event.target.name]: event.target.value
        });
    }


    function startLogin() {
        let flag = 0;
        axios.post(URL, {
            username: user.email,
            password: user.password
        })
            .then(res => {
                setLogin({
                    ...login,
                    "email" : user.email,
                    "data": res.data,
                }); flag = 1;
            })
            .then(() => {if (flag===1) {history.push("/Admin")}})
            .catch(error => {
                console.log(error);
                alert("Email or Password not valid");
            });

    }
    return (
        <div className="content">
            <form className="Loginform">
                <input type="text" className="form-control" onChange={handleChange} name="email" placeholder="Email" /><p></p>
                <input type="password" className="form-control" onChange={handleChange} name="password" placeholder="Password" />
            </form>
            <Link to="/Login"><div id="loginbutton" onClick={() => startLogin()}></div></Link>
            <h6><Link to="/SignUp">Don't have an account? Sign Up</Link></h6>
        </div>
    );
}

export default Login;

