/** USED FOR TESTING AND DEV */

import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
// import { useHistory } from "react-router-dom"

function TestForm() {
  let history = useHistory();
  const currentUser = useContext(UserContext);
  const [info, setLoginInfo] = useState({
    image: "",
  });

  function handleChange(evt) {
    const { name, value } = evt.target;
    setLoginInfo((info) => ({
      ...info,
      [name]: value,
    }));
  }
  // Sends search back to parent component
  function handleSubmit(evt) {
    evt.preventDefault();
    console.log(info)
  }

  console.log( info)
  return (
    <div className="TestForm" style={{ padding: "8px" }}>
      <form className="TestForm" onSubmit={handleSubmit}>
        <div className="form-group">
          <input  
            id="image"
            name="image"
            className="form-control"
            type="file"
            placeholder="image"
            onChange={handleChange}
            value={info.image}
          />
        </div>
        <button className="btn btn-primary"> button </button>
      </form>
    </div>
  );
}

export default TestForm;
