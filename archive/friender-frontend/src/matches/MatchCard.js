import React from "react";
import { Link } from "react-router-dom";
/** MatchCard
 * Card for showing the user's Matches
 *
 * Props:
 *
 * State:
 *
 * { Matches, MatchCarousel } -> MatchCard
 */
export default function MatchCard(props) {
  //FORDEV
  let firstName = props.firstName || "TEST DEV";
  let username = props.username || "TEST USER";
  //END DEV

  return (
    <div className="MatchCard card">

      {/* TODO: Replace firstName with props once created */}
      <Link to={`matches/messages/${username}`}>
        {/* ADD image */}
        <img src="" alt="" />
        {/* TODO: Add user first name display */}
        <h3>{firstName}</h3>

        {/* TODO: Add user User name */}
        {/* TODO: Add user hobbies */}
      </Link>

    </div>
  );
}
