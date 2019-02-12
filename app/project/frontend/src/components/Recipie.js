import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Recipie = ({ data }) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <div className="box">
            <div className="columns">
                <div className="column">
                    <h2 className="subtitle">{data[0].name}</h2>
                    <h3>Serves: {data[0].serves}</h3>
                    <p>{data[0].introduction}</p>
                    <strong>Ingredients</strong>
                    <ul>
                        {data[0].ingredients.map(ingredient => (
                            <li>
                                {ingredient.quantity} {ingredient.unit} of{" "}
                                {ingredient.adjective}{" "}
                                {ingredient.ingredient.name}
                            </li>
                        ))}
                    </ul>
                    <strong>Method</strong>
                    <ol>
                        {data[0].steps.map(step => (
                            <li>{step.text}</li>
                        ))}
                    </ol>
                </div>
            </div>
        </div>
    );

Recipie.propTypes = {
    data: PropTypes.array.isRequired
};

export default Recipie;
