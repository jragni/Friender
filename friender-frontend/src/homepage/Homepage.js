import React from 'react';
import MatchCarousel from "../matches/MatchCarousel";

export default function Homepage(props) {
    return(
        <div className="homepage">
            {/* TODO: add login message */}
            {/* TODO: add login and sign up option if user is not logged in*/}
            <h1> Hello, user</h1>
            <MatchCarousel />
        </div>
    )
}