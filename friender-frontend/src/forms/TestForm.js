/** USED FOR TESTING AND DEV */

import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import axios from "axios"
// import { useHistory } from "react-router-dom"

function TestForm() {
  let history = useHistory();
  const currentUser = useContext(UserContext);
  const [image, setImage] = useState({
    file:""
});

  function handleChange(evt) {
      
    let file = evt.target.files[0]
    setImage((image) => ({ file:file }));
  }
  // Sends search back to parent component
  async function handleSubmit(evt) {
    evt.preventDefault();
    const response = await axios.post("http://localhost:5000/upload", {
      data: image,
    });
    console.log(response)
  }

  console.log(image)
  return (
    <div className="TestForm" style={{ padding: "8px" }}>
      <form className="TestForm" onSubmit={handleSubmit}>
        <div className="form-group">
          <input  
            id="image"
            name="image"
            className="form-control"
            type="file"
            accept=".png, .jpg"
            onChange={handleChange}
            value={image.image} 
          />
        </div>
        <button className="btn btn-primary"> button </button>
      </form>
    </div>
  );
}

export default TestForm;
