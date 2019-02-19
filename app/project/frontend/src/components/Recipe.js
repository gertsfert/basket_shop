import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Recipe = ({ data }) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        data.map(recipe => (
            <div className="box" key={recipe.pk}>
                <div className="columns">
                    <div className="column">
                        <h2 className="subtitle">{recipe.name}</h2>
                        <h3>Serves: {recipe.serves}</h3>
                        <p>{recipe.introduction}</p>
                        <strong>Ingredients</strong>
                        <ul>
                            {recipe.ingredients.map(ingredient => (
                                <li>
                                    {ingredient.quantity} {ingredient.unit} of{" "}
                                    {ingredient.adjective}{" "}
                                    {ingredient.ingredient.name}
                                </li>
                            ))}
                        </ul>
                        <strong>Method</strong>
                        <ol>
                            {recipe.steps.map(step => (
                                <li>{step.text}</li>
                            ))}
                        </ol>
                    </div>
                </div>
            </div>
        ))
    );

Recipe.propTypes = {
    data: PropTypes.array.isRequired
};

export default Recipe;
