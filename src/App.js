import React from "react";
import "./App.css";

import Particles from "react-particles-js";
import particlesParams from "./assets/particlesjs-config.json";

function App() {
  return (
    <div className="App">
      <Particles id="particles" params={particlesParams} />
      <div id="contents">
        <div id="card">
          <img src="gjensidige-logo-v2.png" />
          <div id="buttons">
            <a
              id="btn"
              href="https://forms.gle/rsX8ptiVV7X7ZP6j8"
              target="_blank"
            >
              Registracija dalyviams
            </a>
            <a
              id="btn"
              href="https://forms.gle/KkBfYZ3ddCZDy6ncA"
              target="_blank"
            >
              Siūlyti įdėją
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
