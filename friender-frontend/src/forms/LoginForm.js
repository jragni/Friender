import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
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
      <form className="LoginForm" onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            style={{ width: "400px" }}
            id="email"
            name="image"
            className="form-control"
            placeholder="iamge"
            onChange={handleChange}
            value={loginInfo.image}
          />
        </div>
        <div className="form-group">
          <input
            style={{ width: "400px" }}
            id="login-password"
            name="password"
            className="form-control"
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
