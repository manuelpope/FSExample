import React from 'react';
import {Link} from 'react-router-dom';
import '../styles/SignUp.css';

const SignUp = () =>{
    return(
        <div className="content">
            <form className="SignUpform">
                <input type="text" name="fname" id="fname" placeholder="First Name"/>&emsp;
                <input type="text" name="lname" id="lname" placeholder="Last Name"/><p></p>
                <input type="text" name="country" id="country" placeholder="Country" autoComplete="country"/>&emsp;
                <input type="email" name="email" id="email" placeholder="email" autoComplete="email"/><p></p>
                <input type="password" name="password" placeholder="Password" />&emsp;
                <input type="password" name="password" placeholder="Repeat Password"/>
            </form>
            <Link to="/Login"><td><div id="signupbutton"></div></td></Link>
            <h6><Link to="/Login">Do you have an account? Login In Now!</Link></h6>
        </div>
    );
}

export default SignUp;