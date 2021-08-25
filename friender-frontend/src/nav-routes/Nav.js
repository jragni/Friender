import React, { useContext } from "react";
import "./Nav.css";
import { NavLink } from "react-router-dom";
import UserContext from "../UserContext";

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
        <nav className="Nav navbar navbar-expand-md navbar-dark bg-primary">
          <NavLink exact to="/" className="nav-brand">
            <i> Friender </i>
          </NavLink>

          <ul className="navbar-nav ml-auto">
            <li className="nav-item mr-4">
              <NavLink exact to="/login" className="nav-link">
                Login
              </NavLink>
            </li>
            <li className="navbar-nav mr-4">
              <NavLink exact to="/signup" className="nav-link">
                SignUp
              </NavLink>
            </li>
          </ul>
        </nav>
      }
    </div>
  );
}

export default Nav;
