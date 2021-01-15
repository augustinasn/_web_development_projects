import React, { Component } from "react";

import "./Splash.scss";
import Typed from "typed.js";

export class Splash extends Component {
  constructor(props) {
    super();

    this.state = {
      lang: props.lang,
      strings: {
        lt: {
          typed: [
            "Atsikratykite rankinio darbo.",
            "Pagerinkite savo produktyvumą.",
            "Skirkite daugiau dėmesio svarbioms užduotims."
          ],
          ctaText: "Užpildyti prašymą"
        },
        en: {
          typed: [
            "Get rid of manual work.",
            "Make yourself more productive.",
            "Focus more on what really matters."
          ],
          ctaText: "Fill request form"
        },
        no: {
          typed: [
            "Bli kvitt manuelt arbeid.",
            "Gjør deg mer produktiv.",
            "Fokusere på mer komplekse oppgaver."
          ],
          ctaText: "Fyll ut forespørsel"
        }
      }
    };
  }

  render() {
    return (
      <div className="Splash">
        <div id="splash-content">
          <div id="typed-div">
            <h1 id="typed"></h1>
          </div>
          <a
            id="cta"
            href="https://forms.gle/6xDyydQZF6D614g89"
            target="_blank"
          >
            {this.state.strings[this.state.lang].ctaText}
          </a>
        </div>
        <div id="color-overlay"></div>
      </div>
    );
  }

  componentDidMount() {
    // Typed.js

    var options = {
      strings: this.state.strings[this.state.lang].typed,
      typeSpeed: 40,
      loop: true,
      backSpeed: 40,
      backDelay: 1000
    };

    var typed = new Typed("#typed", options);
  }
}

export default Splash;
