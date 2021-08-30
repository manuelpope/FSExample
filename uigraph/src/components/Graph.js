import React, { useState } from 'react';
import Button from '@material-ui/core/Button';
import { useHistory } from "react-router-dom";
import { useEffect } from 'react'; import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import '../styles/main.css';

const Graphic = () => {
  const [stateAmount, setStateAmount] = useState([]);
  const [stateQuant, setStateQuant] = useState([]);
  const history = useHistory();

  const uri1 = '/seriesresume';
  let flag;

  const apiGet = (setStateAmount,setStateQuant) => {
    fetch(uri1, {
      headers: {
        'Accept': 'application/json'
      }
    })
      .then(res =>
        res.json())


      .then(data => {
        //console.log("dataSeries: ",data)

        setStateAmount(dataExtraction(data,'amount'))

        setStateQuant(dataExtraction(data,''))
      }
      ).catch(err => console.log(err));
  };


  useEffect(() => {

    apiGet(setStateAmount, setStateQuant);









  }, []);

	const redirectHome = () => {
		history.push('/Admin');
	  }
		;

  return (


    <div className='big-screen'>

      {stateAmount &&

<ResponsiveContainer width="80%" height="95%">
        <LineChart
       
          data={stateAmount}
          margin={{
            top: 50 ,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >

          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="amount" stroke="#8884d8" activeDot={{ r: 8 }} />
        </LineChart>
        </ResponsiveContainer>
      }
      {stateQuant &&

      <ResponsiveContainer width="80%" height="95%">

        <LineChart

          data={stateQuant}
          margin={{
            top: 50,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
         

          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="quantity" stroke="#8884d8" activeDot={{ r: 8 }} />
        </LineChart>
        </ResponsiveContainer>

      }
          <Button id='backbuttongraph' size='large' onClick={redirectHome} variant="outlined" color="secondary">
                Back
          </Button>

    </div>

  );


}

export default Graphic;

function dataExtraction(data, flag) {
  let resultAmount = [];

  if(flag==='amount'){
    for (var i in data.items.amountPerMonthAllStores)
    resultAmount.push(new Object({
      name: i.toString(),
      amount: data.items.amountPerMonthAllStores[i]
    }));
    return resultAmount;
  }

  for (var i in data.items.amountPerMonthAllStores)
    resultAmount.push(new Object({
      name: i.toString(),
      quantity: data.items.quantityPerMonthAllStores[i]
    }));
    return resultAmount;
}
