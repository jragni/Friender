import React from 'react';
import MatchCard from './MatchCard';

/** MatchCarousel
 * The component that shows the potential friends the user can match with.
 */
export default function MatchCarousel(props) {

    return(
        // TODO: add jumbotron for carrousel
        <div className="MatchCarousel">
            <MatchCard />
            {/* TODO: create an api for this  */}
            <button>Interested</button>
            <button>No thank you</button>
        </div>
    )
}