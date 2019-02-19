import React from "react";

const RecipeSummaryCard = ({ recipe }) => (
    <div className="card">
        <header className="card-header">
            <p className="card-header-title">{recipe.name}</p>
        </header>
        <div className="card-content">
            <div className="content">
                <h4>Serves: {recipe.serves}</h4>
                <p>{recipe.introduction}</p>
            </div>
        </div>
    </div>
);

export default RecipeSummaryCard;
