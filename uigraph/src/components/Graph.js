import React, { useState } from 'react';
import { useEffect } from 'react'; import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';


const Graphic = () => {
  const [stateAmount, setStateAmount] = useState([]);
  const [stateQuant, setStateQuant] = useState([]);

  const uri1 = '/seriesresume';

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
        var resultAmount = [];
        var resultQuant = [];


        for (var i in data.items.amountPerMonthAllStores)
          resultAmount.push(new Object({
            name: i.toString(),
            amount: data.items.amountPerMonthAllStores[i]
          }));
        for (var i in data.items.amountPerMonthAllStores)
          resultQuant.push(new Object({
            name: i.toString(),
            quantity: data.items.quantityPerMonthAllStores[i]
          }));


        setStateAmount(resultAmount)

        setStateQuant(resultQuant)
      }
      ).catch(err => console.log(err));
  };


  useEffect(() => {

    apiGet(setStateAmount, setStateQuant);









  }, []);



  return (


    <div>
      {stateAmount &&
        <LineChart
          width={1500}
          height={300}
          data={stateAmount}
          margin={{
            top: 5,
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
      }
      {stateQuant &&
        <LineChart
          width={1500}
          height={300}
          data={stateQuant}
          margin={{
            top: 5,
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
      }

    </div>

  );


}

export default Graphic;