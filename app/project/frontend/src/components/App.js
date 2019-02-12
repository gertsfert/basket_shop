import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Recipie from "./Recipie";
const App = () => (
  <DataProvider
    endpoint="recipies/api/recipie/"
    render={data => <Recipie data={data} />}
  />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
