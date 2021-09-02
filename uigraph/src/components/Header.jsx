import React, {useContext} from 'react';
import {Link} from 'react-router-dom';
import '../styles/Header.css';
import logo from '../styles/static/Logo.png';
import AppContext from '../context/AppContext';


function Header(){
    const {login} = useContext(AppContext);

    return(
        <div className="topnav">
              
              <Link to="/"><img className="logo" src={logo} alt=""/></Link>  
               <h1 className="title"><Link to="/">-Dash Now-</Link></h1>
                {login.data.access_token===null && <div>
               <h2 className="Login"><Link to="/Login">Login</Link></h2>
                </div>}
               {login.data.access_token!==null && <div>
               <h2 className="user"><Link to="/Logout">Hello! {login.email}, Logout</Link></h2>
                </div>}
            
        </div>
    )
}

export default Header;