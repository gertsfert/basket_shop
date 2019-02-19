import React from "react";
import PropTypes from "prop-types";
import RecipeSummaryCard from "./RecipeSummaryCard";

const Recipe = ({ data }) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <div className="columns">
            <div className="column">
                {data.map(recipe => (
                    <div key={recipe.id}>
                        <RecipeSummaryCard recipe={recipe} />
                    </div>
                ))}
            </div>
        </div>
    );

Recipe.propTypes = {
    data: PropTypes.array.isRequired
};

export default Recipe;
