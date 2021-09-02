import React,{useContext} from 'react';
import '../styles/Login.css';
import {useHistory } from 'react-router-dom';
import AppContext from '../context/AppContext';

const URL = "/logout";

const Logout = () =>{

    const {login,setLogin} = useContext(AppContext);
    let history = useHistory();

    function closeSession(){
        fetch(URL, { 
            method: 'post', 
            headers:{
              'Authorization': 'Bearer '+login.data.access_token
            }, 
          })
            .then(
                setLogin({
                    "id":0,
                    "fname":"",
                    "lname":"",
                    "country":"",
                    "email":"",
                    "data":{access_token:null,refresh_token:null}
                })
            )
            .catch(error => {
                alert(error);
            });
            
    }

    return(
        <div className="content">
            {closeSession()}
            {history.push("/")}
        </div>
    );
}

export default Logout;

