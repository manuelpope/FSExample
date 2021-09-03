import React,{useState} from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import TableData from '../components/Table';
import Graphic from '../components/Graph';
import SaveList from '../components/DailyInfo';
import '../styles/App.css';
import Home from '../containers/Home';
import Admin from '../containers/Admin';
import Data from '../containers/Data';
import Profile from '../containers/Profile';
import Alerts from '../containers/Alerts';
import Kpis from '../containers/Kpis';
import About from '../containers/About';
import Login from '../containers/Login';
import Logout from '../containers/Logout';
import SignUp from '../containers/SignUp';
import NotFound from '../containers/NotFound';
import Layout from '../components/Layout';
import AppContext from '../context/AppContext';
import {Helmet} from "react-helmet";

function App() {

  const [login,setLogin]=useState({
    "id":0,
    "fname":"",
    "lname":"",
    "country":"",
    "email":"",
    "data":{access_token:null,refresh_token:null}
});

  return (
    <AppContext.Provider value={{login,setLogin}}>
    <Helmet>
        <title>-Dash Now-</title>
        <meta
            name = "description"
            content = "Get your own Dashboard now!" 
        />
        <meta name="keywords" content="Data, AI, Dashboards, math models, data visualization"/>
    </Helmet>
    <BrowserRouter>
        <Layout>          
          <Switch>                  
              <Route exact path="/" component={Home} />
              <Route exact path='/Admin' component={Admin}/>
              <Route exact path='/Data' component={Data}/>
              <Route exact path='/table' component={TableData}/>
              <Route exact path='/profile' component={Profile}/>
              <Route exact path='/alerts' component={Alerts}/>
              <Route exact path='/kpis' component={Kpis}/>
              <Route exact path='/about' component={About}/>
              <Route exact path='/graph' component={Graphic}/>
              <Route exact path='/graph' component={Graphic}/>
              <Route exact path='/remote' component={SaveList}/>
              <Route exact path="/Login" component={Login} />
              <Route exact path="/Logout" component={Logout} />
              <Route exact path="/SignUp" component={SignUp} />
              <Route component={NotFound} />
          </Switch>
        </Layout>
    </BrowserRouter>
    </AppContext.Provider>
  );
}

export default App;
