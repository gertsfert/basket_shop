import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Recipe = ({ data }) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <div className="columns">
            <div className="column">
                {data.map(recipe => (
                    <div className="box" key={recipe.id}>
                        <div className="columns">
                            <div className="column">
                                <h2 className="subtitle">{recipe.name}</h2>
                                <h3>Serves: {recipe.serves}</h3>
                                <p>{recipe.introduction}</p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );

Recipe.propTypes = {
    data: PropTypes.array.isRequired
};

export default Recipe;
