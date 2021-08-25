import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import "./LoginForm.css";
// import { useHistory } from "react-router-dom"

function LoginForm() {
  let history = useHistory();
  const { login } = useContext(UserContext);
  const [loginInfo, setLoginInfo] = useState({
    email: "",
    password: "",
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
    history.push("/");
  }

  return (
    <div className="LoginForm" style={{ padding: "8px" }}>
      <form className="login-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            style={{ width: "400px" }}
            id="email"
            name="email"
            className="form-control form-input"
            placeholder="Email"
            onChange={handleChange}
            value={loginInfo.email}
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            style={{ width: "400px" }}
            id="login-password"
            name="password"
            className="form-control form-input"
            placeholder="Password"
            onChange={handleChange}
            value={loginInfo.password}
          />
        </div>
        <button className="btn-primary btn">Log In</button>
      </form>
    </div>
  );
}

export default LoginForm;
