import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Recipie = ({ data }) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        data.map(recipie => (
            <div className="box">
                <div className="columns">
                    <div className="column">
                        <h2 className="subtitle">{recipie.name}</h2>
                        <h3>Serves: {recipie.serves}</h3>
                        <p>{recipie.introduction}</p>
                        <strong>Ingredients</strong>
                        <ul>
                            {recipie.ingredients.map(ingredient => (
                                <li>
                                    {ingredient.quantity} {ingredient.unit} of{" "}
                                    {ingredient.adjective}{" "}
                                    {ingredient.ingredient.name}
                                </li>
                            ))}
                        </ul>
                        <strong>Method</strong>
                        <ol>
                            {recipie.steps.map(step => (
                                <li>{step.text}</li>
                            ))}
                        </ol>
                    </div>
                </div>
            </div>
        ))
    );

Recipie.propTypes = {
    data: PropTypes.array.isRequired
};

export default Recipie;
