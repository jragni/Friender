/** USED FOR TESTING AND DEV */

import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
// import { useHistory } from "react-router-dom"

function TestForm() {
  let history = useHistory();
  const currentUser = useContext(UserContext);
  const [loginInfo, setLoginInfo] = useState({
    image: "",
  });

  function handleChange(evt) {
    const { name, value } = evt.target;
    setLoginInfo((loginInfo) => ({
      ...loginInfo,
      [name]: value,
    }));
  }
  // Sends search back to parent component
  function handleSubmit(evt) {
    evt.preventDefault();
    //login(loginInfo);
  }

  return (
    <div className="TestForm" style={{ padding: "8px" }}>
      <form className="TestForm" onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            id="image"
            name="image"
            className="form-control"
            placeholder="image"
            onChange={handleChange}
            value={loginInfo.image}
          />
        </div>
        <button className="btn btn-primary"> button </button>
      </form>
    </div>
  );
}

export default TestForm;
