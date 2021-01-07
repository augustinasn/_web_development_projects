import React, { useState } from "react";
import axios from "axios";

import "./App.css";

export default function App() {
  const [currentAutist, setCurrentAutist] = useState("-");
  const [currentText, setCurrentText] = useState("");
  const [displayedText, setDisplayedText] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  function handleChange(e) {
    setCurrentText(e.target.value);
  }

  function handleSubmit(e) {
    e.preventDefault();

    if (isLoading) {
      return;
    }

    setCurrentText("");

    let searchUrl = "https://autizmas-api.herokuapp.com/predict_autist";
    let formData = new FormData();

    formData.append("text", currentText);

    let config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };

    setIsLoading(true);

    axios.post(searchUrl, formData, config).then((res) => {
      setDisplayedText(currentText);
      setCurrentAutist(res.data);
      setIsLoading(false);
    });
  }

  return (
    <div className="App">
      <h1>Autist Identifier v1.0</h1>
      <div id="response-div">
        <div id="input-side">
          <h3>Input:</h3>
          {isLoading ? <img src="loading.gif" /> : <h2>{displayedText}</h2>}
        </div>
        <div id="output-side">
          <h3>Prediction:</h3>
          {isLoading ? <img src="loading.gif" /> : <h2>{currentAutist}</h2>}
        </div>
      </div>
      <div id="text-div">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="input-text"
            value={currentText}
            onChange={handleChange}
            placeholder="Type some text to predict and press enter/submit button..."
          ></input>
          <input type="submit" value="Predict"></input>
        </form>
      </div>
    </div>
  );
}
