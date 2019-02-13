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
                    </div>
                </div>
            </div>
        ))
    );

Recipie.propTypes = {
    data: PropTypes.array.isRequired
};

export default Recipie;
