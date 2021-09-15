import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import React, { useState } from 'react';
import { useEffect } from 'react';
import Button from '@material-ui/core/Button';
import { useHistory } from "react-router-dom";
import '../styles/main.css';


const TableData = () => {


  const [stateSucursal, setStateSucursal] = useState([]);
  const history = useHistory();

  const uri2 = '/storesresume';
  const uri1 = '/stores';

  const apiGet = (setState, uri) => {
    fetch(uri, {
      headers: {
        'Accept': 'application/json'
      }
    })
      .then(res =>
        res.json())


      .then(data => {

        console.log(data)
        var result = [];

        for (var i in data.sucursales) {

          result.push(
            data.sucursales[i]
          );
        };

        const listSales = result.map(element => {
          let sales = []
          for (var i in element.salesMonthly) {
            const obj = new Object({
              name: element.name,
              address: element.address,
              telf: element.telf,
              mes: i,
              quant: element.quantityMonthly[i],
              sales: element.salesMonthly[i]
            });


            sales.push(obj);
          };
          return sales
        }).flat();







        setState(listSales)

      }
      ).catch(err => console.log(err));
  };


  useEffect(() => {

    apiGet(setStateSucursal, uri2);







  }, []);


  const useStyles = makeStyles({
    table: {
      minWidth: 650,
    },
  });

	const redirectHome = () => {
		history.push('/Admin');
	  }
		;

  return (
    <TableContainer component={Paper}>
      <Table className={useStyles.table} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>

            <TableCell align="right">nombre</TableCell>
            <TableCell align="right">direccion&nbsp;</TableCell>
            <TableCell align="right">telf&nbsp;(#)</TableCell>
            <TableCell align="right">mes&nbsp;</TableCell>
            <TableCell align="right">monto&nbsp;($)</TableCell>
            <TableCell align="right">ventas&nbsp;</TableCell>


          </TableRow>
        </TableHead>
        <TableBody>
          {stateSucursal.map((row) => (
            <TableRow key={row.index}>
              <TableCell component="th" scope="row" align="right">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.address}</TableCell>
              <TableCell align="right">{row.telf}</TableCell>
              <TableCell align="right">{row.mes}</TableCell>
              <TableCell align="right">{row.sales}</TableCell>
              <TableCell align="right">{row.quant}</TableCell>

            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Button id='backbuttontable' size='large' onClick={redirectHome} variant="outlined" color="secondary">
          Back
      </Button>
    </TableContainer>
  );
}

export default TableData;