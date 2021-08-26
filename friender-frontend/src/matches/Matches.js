import React, { useContext, useState } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import Match from "./Match";

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

  const [matches, setMatches] = useState([1, 2, 3, 4, 5, 6]);

  /** TODO: fetch list of user's matches from the API
  /* TODO: add */

  return (
    <div className="Matches container">
      <h1>
        <i>
          <u> Your Matches</u>
          {matches.map((m) => (
            <Match match={m} />
          ))}
        </i>
      </h1>
    </div>
  );
}

export default Matches;
