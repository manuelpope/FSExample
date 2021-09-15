import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import { useHistory } from "react-router-dom";






const OutlinedButtons = () => {

  const history = useHistory();


  const useStyles = makeStyles((theme) => ({
    root: {
      '& > *': {
        margin: theme.spacing(1),
      },
    },
  }));
  const redirectHome = () => {

    console.log('moving to home');
    history.push('/');
  }
    ;
  const redirectTable = () => {

    console.log('moving to table');
    history.push('/table');
  }
    ;
  const redirectGraph = () => {

    console.log('moving to graph');
    history.push('/graph');
  }
    ;



  return (
    <div className={useStyles.root}>
      <Button onClick={redirectHome} variant="outlined" color="primary" >
        Home
      </Button>
      <Button onClick={redirectTable} variant="outlined" color="secondary">
        Table
      </Button>
      <Button onClick={redirectGraph} variant="outlined" color="secondary">
        Graph
      </Button>
    </div>
  );
}
export default OutlinedButtons;
