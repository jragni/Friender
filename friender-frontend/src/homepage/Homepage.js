import "./Homepage.css";
import React, { useContext } from "react";
import MatchCarousel from "../matcher/MatchCarousel";
import UserContext from "../UserContext";
import { Link } from "react-router-dom";

/** Homepage
 * Displays the homepage of the application where user can begini to find matches.
 *
 * State: none;
 * Props:
 *  like
 *  dislike
 *
 *  Routes -> Hompage -> MatchCarousel
 */
function Homepage() {
  const currentUser = useContext(UserContext);

  console.log("currentUser hompage: ", currentUser);
  return (
    <div className="Homepage">
      {currentUser ? (
        <MatchCarousel />
      ) : (
        <div className="container homepage-jumbotron">
          <main className="card container">
            <div className="card-body">
              <h1> Friendster </h1>
              <h4 className="card-subtitle text-muted">
                ~Meet lonely adults in your area~
              </h4>
              <div className="card-body">
                <Link className="btn btn-login btn-lg" to="/login">
                  Log In
                </Link>
                <Link className="btn btn-signup btn-lg" to="/signup">
                  Sign Up
                </Link>
              </div>
            </div>
          </main>
        </div>
      )}
    </div>
  );
}

Homepage.defaultProps = {
  currentUser: { firstName: "testFN", lastName: "testLN" },
};

export default Homepage;
