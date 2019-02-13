import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import RecipieBrowse from "./RecipieBrowse";
const App = () => (
    <DataProvider
        endpoint="recipies/api/recipies/"
        render={data => <RecipieBrowse data={data} />}
    />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
