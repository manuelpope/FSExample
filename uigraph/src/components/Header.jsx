import React, {useContext, useState} from 'react';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import {Link} from 'react-router-dom';
import '../styles/Header.css';
import logo from '../styles/static/Logo.png';
import AppContext from '../context/AppContext';

function Header(){
    const {login} = useContext(AppContext);
    const [anchorEl, setAnchorEl] = useState(null);
    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
      };
    
      const handleClose = () => {
        setAnchorEl(null);
      };  

    return(
        <div className="topnav">
              
              <Link to="/"><img className="logo" src={logo} alt=""/></Link>  
               <h1 className="title"><Link to="/">-Dash Now-</Link></h1>
                {login.data.access_token===null && <div>
                    <h2 id="Login">
                    <Button aria-controls="simple-menu" aria-haspopup="true" onClick={handleClick}>
                    <h2>Menu</h2>
                    </Button>
                    <Menu
                        id="simple-menu"
                        className="Option"
                        anchorEl={anchorEl}
                        keepMounted
                        open={Boolean(anchorEl)}
                        onClose={handleClose}
                    >
                        <MenuItem onClick={handleClose}><Link to="/Login">Login</Link></MenuItem>
                        <MenuItem onClick={handleClose}><Link to="/about">About Us</Link></MenuItem>
                    </Menu>
                    </h2>
                </div>}
               {login.data.access_token!==null && <div>
                <h2 id="Login2">
                    <Button aria-controls="simple-menu" aria-haspopup="true" onClick={handleClick}>
                    <h3>Hello! {login.email}</h3>
                    </Button>
                    <Menu
                        id="simple-menu"
                        className="Option"
                        anchorEl={anchorEl}
                        keepMounted
                        open={Boolean(anchorEl)}
                        onClose={handleClose}
                    >
                        <MenuItem onClick={handleClose}><Link to="/profile">Profile</Link></MenuItem>
                        <MenuItem onClick={handleClose}><Link to="/alerts">Alerts</Link></MenuItem>
                        <MenuItem onClick={handleClose}><Link to="/kpis">KPI's</Link></MenuItem>
                        <MenuItem onClick={handleClose}><Link to="/about">About Us</Link></MenuItem>
                        <MenuItem onClick={handleClose}><Link to="/Logout">Log Out</Link></MenuItem>
                    </Menu>
                    </h2>
               <h2 className="user"><Link to="/Logout">Hello! {login.email}, Logout</Link></h2>
                </div>}
            
        </div>
    )
}

export default Header;
