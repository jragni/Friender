import React, { useContext, useState } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import MatchCard from "./MatchCard";

// FOR DEV TESTING ---- delete later
const userTest1 = {
  id: 1,
  firstName: "test1FN",
  lastName: "test1LN",
  description: "I love dogs.",
};
const userTest2 = {
  id: 2,
  firstName: "test2FN",
  lastName: "test2LN",
  description: "I love cats.",
};
const userTest3 = {
  id: 3,
  firstName: "test3FN",
  lastName: "test3LN",
  description: "I love tacos.",
};
const userTest4 = {
  id: 4,
  firstName: "test4FN",
  lastName: "test4LN",
  description: "I love large intestines.",
};

// END DEV TESTING

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
  const [matches, setMatches] = useState([
    userTest1,
    userTest2,
    userTest3,
    userTest4,
  ]);
  /** TODO: fetch list of user's matches from the API */
  return (
    <div className="Matches container">
      <h1>
        <i>Your Matches</i>
      </h1>
      {matches.length === 0 ? (
        <i> No matches? Keep Trying {"<3"}</i>
      ) : (
        matches.map((m, idx) => <MatchCard key={m.id} match={m} />)
      )}
      )
    </div>
  );
}

export default Matches;
