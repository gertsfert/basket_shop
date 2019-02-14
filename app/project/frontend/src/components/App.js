import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import RecipeBrowse from "./RecipeBrowse";
const App = () => (
    <DataProvider
        endpoint="recipes/api/recipes/"
        render={data => <RecipeBrowse data={data} />}
    />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
