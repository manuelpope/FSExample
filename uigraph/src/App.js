import logo from './logo.svg';
import OutlinedButtons from './components/ButtonTAB'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import HomePage from './components/HomePage';
import TableData from './components/Table';
import Graphic from './components/Graph';
import SaveList from './components/DailyInfo';


function App() {


  return (
    <Router>
      <div>

        <OutlinedButtons />


        <Switch>
          <Route exact path='/' component={HomePage}></Route>
          <Route exact path='/table' component={TableData}></Route>
          <Route exact path='/graph' component={Graphic}></Route>
          <Route exact path='/graph' component={Graphic}></Route>
          <Route exact path='/remote' component={SaveList}></Route>

        </Switch>



      </div>
    </Router>

  );
}

export default App;
