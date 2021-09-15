import React,{useContext} from 'react';
import {Link} from 'react-router-dom';
import OutlinedButtons from '../components/ButtonTAB';
import '../styles/Admin.css';
import AppContext from '../context/AppContext';

const Admin = () =>{

  const {login} = useContext(AppContext);
  return (
    <div>
        {/*login.data.access_token===null && <div>          
          {window.location.href="/Login"}
        </div>*/}    
        {login.data.access_token===null && <div>
          <h1 id='title'>Main Panel</h1>
          <OutlinedButtons /> 
        </div>}
    </div>
  );
}

export default Admin;