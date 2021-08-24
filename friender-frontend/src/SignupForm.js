import React, { useState, useContext } from "react";
import UserContext from "./UserContext";
// import { useHistory } from "react-router-dom";

function SignUpForm() {
  // let history = useHistory()
  const { signup } = useContext(UserContext);
  const [signUpInfo, setSignUpInfo] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  function handleChange(evt) {
    const { name, value } = evt.target;
    setSignUpInfo((SignUpData) => ({
      ...SignUpData,
      [name]: value,
    }));
  }
  // Sends search back to parent component
  function handleSubmit(evt) {
    evt.preventDefault();
    signup(signUpInfo);
    // if(currentUser) history.push("/companies")
  }

  return (
    <div className="SignUpForm" style={{ padding: "8px" }}>
      <form className="Sign-up-page" onSubmit={handleSubmit}>
        <input
          style={{ width: "400px" }}
          id="Sign-up-first-name"
          name="firstName"
          className="form-control"
          placeholder="First Name"
          onChange={handleChange}
          value={signUpInfo.firstName}
        />
        <input
          style={{ width: "400px" }}
          id="Sign-up-last-name"
          name="lastName"
          className="form-control"
          placeholder="Last Name"
          onChange={handleChange}
          value={signUpInfo.lastName}
        />
        <input
          style={{ width: "400px" }}
          id="Sign-up-email"
          name="email"
          className="form-control"
          placeholder="Email"
          onChange={handleChange}
          value={signUpInfo.email}
        />
        <input
          style={{ width: "400px" }}
          id="Sign-up-password"
          name="password"
          className="form-control"
          placeholder="Password"
          onChange={handleChange}
          value={signUpInfo.password}
        />
        <button>Register to meet lonely friends</button>
      </form>
    </div>
  );
}

export default SignUpForm;
