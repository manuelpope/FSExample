import logo from './logo.svg';
import './App.css';
import OutlinedButtons from './components/ButtonTAB'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import HomePage from './components/HomePage';
import TableData from './components/Table';
import Graphic from './components/Graph';


function App() {


  return (
    <Router>
      <div>

        <OutlinedButtons />


        <Switch>
          <Route exact path='/' component={HomePage}></Route>
          <Route exact path='/table' component={TableData}></Route>
          <Route exact path='/graph' component={Graphic}></Route>

        </Switch>



      </div>
    </Router>

  );
}

export default App;
