import "./Homepage.css";
import React, { useContext } from "react";
import MatchCarousel from "../matcher/MatchCarousel";
import NotLogged from "./NotLogged";
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
      {console.log(currentUser)}
      {currentUser ? <MatchCarousel /> : <NotLogged />}
    </div>
  );
}

Homepage.defaultProps = {
  currentUser: { firstName: "testFN", lastName: "testLN" },
};

export default Homepage;
