import React, { Component } from "react";
import * as d3 from "d3";

import "./Chart.scss";

class Chart extends Component {
  componentDidMount() {
    // Source - https://bl.ocks.org/gordlea/27370d1eea8464b04538e6d8ced39e89

    var margin = { top: 30, right: 30, bottom: 30, left: 30 },
      width = 800 - margin.left - margin.right,
      height = 225 - margin.top - margin.bottom;

    var n = 15;

    var xScale = d3
      .scaleLinear()
      .domain([1, n])
      .range([0, width]);

    var yScale = d3
      .scaleLinear()
      .domain([0, 100])
      .range([height, 0]);

    var line = d3
      .line()
      .x(function(d, i) {
        return xScale(i + 1);
      })
      .y(function(d) {
        return yScale(d.y);
      })
      .curve(d3.curveMonotoneX);

    var dataset = d3.range(n).map(function(d) {
      return { y: d3.randomUniform(100)() };
    });

    var svg = d3
      .select(".Chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg
      .append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(xScale));

    svg
      .append("g")
      .attr("class", "y axis")
      .call(d3.axisLeft(yScale));

    svg
      .append("path")
      .datum(dataset)
      .attr("class", "line")
      .attr("d", line);

    svg
      .selectAll(".dot")
      .data(dataset)
      .enter()
      .append("circle")
      .attr("class", "dot")
      .attr("cx", function(d, i) {
        return xScale(i + 1);
      })
      .attr("cy", function(d) {
        return yScale(d.y);
      })
      .attr("r", 5);
  }
  render() {
    return <div className="Chart"></div>;
  }
}

export default Chart;
