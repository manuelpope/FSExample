import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import { useHistory } from "react-router-dom";
import '../styles/Admin.css';






const OutlinedButtons = () => {

  const history = useHistory();


  const useStyles = makeStyles((theme) => ({
    root: {
      '& > *': {
        margin: theme.spacing(1),
      },
    },
  }));
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
    const redirectUpload = () => {

      console.log('moving to graph');
      history.push('/Data');
    }
      ;


  return (
    <div className={useStyles.root}>
      <Button id='button1' size='large' onClick={redirectUpload} variant="outlined" color="primary" >
        Upload
      </Button>
      <Button id='button2' size='large' onClick={redirectTable} variant="outlined" color="secondary">
        Table
      </Button>
      <Button id='button3' size='large' onClick={redirectGraph} variant="outlined" color="secondary">
        Graph
      </Button>
    </div>
  );
}
export default OutlinedButtons;
