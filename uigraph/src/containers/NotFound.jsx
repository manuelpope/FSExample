import React from 'react';
import '../styles/NotFound.css';
import Sadface from '../styles/static/Sadface.png';

const NotFound = () =>{
    return (
        <div className="content">
            <img className="SadFace" src={Sadface} alt="SadFace"/>        
            <h1>404 Page Not Found</h1>
        </div>
    );
}

export default NotFound;