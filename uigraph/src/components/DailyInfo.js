import React, { useEffect, useState } from 'react'

export const SaveList= () => {
  // set up local state for generating the download link
  const downloadLink ='/remote';
  const [state, setState] = useState("Loading")
  // function for generating file and set download link
  const makeTextFile = (setState) => {
     
    fetch(downloadLink,{
method:"GET",
    
headers:{
    "Accept": "text/plain",
    "Access-Control-Allow-Methods": "GET",

}})
    .then(res =>
        //console.log(res)) 
        res.text())
        .then(r=>setState(r))
    // update the download link state

  }

  // Call the function if list changes
  useEffect(() => {
    makeTextFile(setState)
  }, [])

  return (
    <div>
        <p>{state}</p>
    </div>
    
  )
}

export default SaveList