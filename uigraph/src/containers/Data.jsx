import React, {useState, useContext} from 'react';
import {Link} from 'react-router-dom';
import '../styles/Data.css';
import AppContext from '../context/AppContext';

function Data(){

	const {login} = useContext(AppContext);
	const [selectedFile, setSelectedFile] = useState();
	const [isSelected, setIsSelected] = useState(false);

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsSelected(true);
	};

	const handleSubmission = () => {
		let formData = new FormData();

		formData.append('file', selectedFile);
		formData.append('name',"test");
		formData.append('target',"price");
		console.log(formData);
		console.log(selectedFile);
		const URL='http://localhost:8081/addCsv';
		fetch(
			//Acá debe ir el link de la API
			URL,{
				method: 'POST',	
				mode: 'no-cors',
				body: formData
			}
		)
	};

	return(
		<div>
			{login.data.access_token===null && <div>
			{window.location.href="/Login"}
			</div>}    
			{login.data.access_token!==null && <div>
			<div className="upload">
				<input className="Button" type="file" name="file" onChange={changeHandler}/>
				{isSelected ? (
					<div className="info">
						<br/><b style={{color: '#f79533'}}>File Name:</b> {selectedFile.name}<br/><br/>
						<b style={{color: '#f37055'}}>File Type:</b> {selectedFile.type}<br/><br/>
						<b style={{color: '#ef4e7b'}}>Size:</b> {selectedFile.size} Bytes<br/><br/>
						<b style={{color: '#5073b8'}}>last Modified Date:{' '}</b> {selectedFile.lastModifiedDate.toLocaleDateString()}<br/><br/>
						
					</div>
				) : (
					<p>Select a file to show details</p>
				)}
				<div>
					<button className="ButtonSubmit" onClick={handleSubmission}>Submit</button>
				</div>            
			</div>
			<Link to="/Admin"><div id="backbutton"></div></Link>
		</div>}
	  </div>
	)
}
export default Data;