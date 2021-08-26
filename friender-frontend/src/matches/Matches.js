import React, { useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";

/** Matches
 * Show the current user's matches
 *
 * Props:
 *  - getMatches --- function to get users matches
 * Routes -> Matches
 */

function Matches({ getMatches }) {
  const currentUser = useContext(UserContext);
  const history = useHistory();
  if (!currentUser) history.push("/");
  /** TODO: fetch list of user's matches from the API
  /* TODO: add */

  return <div className="Matches"> DEV IN PROGRESS </div>;
}

export default Matches;
