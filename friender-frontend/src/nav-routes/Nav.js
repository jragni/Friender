import React, { useContext } from "react";
import { NavLink } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.css";
import UserContext from "./UserContext";

/** Nav: navbar for each page
 *
 *  Props:
 *  -
 */
//TODO pass logout function through the nav props
// and add it as an onclick event on the logout button
function Nav() {
  const { logout, currentUser } = useContext(UserContext);
  return (
    <div className="Navbar">
      {
        <nav className="Nav navbar navbar-expand-lg navbar-light bg-light">
          <NavLink exact to="/" className="nav-brand">
            Friender.. Find hot lonely friends nearby.... they're waiting.
          </NavLink>
          <NavLink exact to="/login" className="nav-link">
            Login
          </NavLink>
          <NavLink exact to="/signup" className="nav-link">
            SignUp
          </NavLink>
        </nav>
      }
    </div>
  );
}

export default Nav;
