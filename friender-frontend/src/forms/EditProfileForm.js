import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import "./EditProfileForm.css";

/**EditProfileForm
 * form for users to edit their profile. In order to edit profile, user
 * must enter correct password.
 *
 * Props:
 * - update --- function to update the current user profile.
 * States:
 *  - userInfo  --- form fields {firstName, lastName, email, password}
 *
 * Routes -> EditProfileForm
 */
function EditProfileForm({ update }) {
  console.log("EditProfileForm: rendering");

  const history = useHistory();
  const currentUser = useContext(UserContext);
  let { firstName, lastName, email, description, zip, radius } = currentUser;
  description = description || "";
  if (!currentUser) history.push("/");

  // STATES
  const [userInfo, setUserInfo] = useState({
    firstName,
    lastName,
    email,
    password: "",
    description,
    zip,
    radius,
  });

  function handleChange(evt) {
    const { name, value } = evt.target;
    setUserInfo((userInfo) => ({
      ...userInfo,
      [name]: value,
    }));
  }

  /** submits user updates to api, will flash error if password is invalid */
  function handleSubmit(evt) {
    evt.preventDefault();
    try {
      update(userInfo);
      history.push("/");
    } catch {
      //TODO: handle invalid password
    }
  }

  return (
    <div className="EditProfileForm">
      <form className="container EditProfileForm-form" onSubmit={handleSubmit}>
        <h1> Edit Profile </h1>

        <input
          id="user-first-name"
          name="firstName"
          className="form-control form-input"
          placeholder="First Name"
          onChange={handleChange}
          value={userInfo.firstName}
        />

        <input
          id="user-last-name"
          name="lastName"
          className="form-control form-input"
          placeholder="Last Name"
          onChange={handleChange}
          value={userInfo.lastName}
        />

        <input
          id="user-email"
          name="email"
          className="form-control form-input"
          placeholder="Email"
          onChange={handleChange}
          value={userInfo.email}
          readOnly
        />
        <input
          id="signup-radius"
          type="number"
          min="10"
          max="100"
          name="radius"
          className="form-control form-input"
          placeholder="Friend search radius? (miles)"
          onChange={handleChange}
          value={userInfo.radius}
        />
        <input
          id="signup-zip"
          name="zip"
          pattern="[0-9]{5}"
          className="form-control form-input"
          placeholder="Your ZIP code"
          onChange={handleChange}
          value={userInfo.zip}
        />

        <textarea
          id="user-description"
          name="description"
          className="form-control form-input"
          placeholder="Tell us about yourself..."
          onChange={handleChange}
          value={userInfo.description}
        />

        <input
          id="user-password"
          name="password"
          type="password"
          className="form-control form-input"
          placeholder="Password"
          onChange={handleChange}
          value={userInfo.password}
          required
        />
        <button className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
}

export default EditProfileForm;
