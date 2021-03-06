import React from "react";
import { render, screen } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";

import App from "../../components/App";

describe("< /> tests", () => {
  it("should render the dashboard page", () => {
    render(
      <Router>
        <App />
      </Router>
    );

    const header = screen.getByTestId("app-header");
    const nav = screen.getByTestId("app-nav");
    const content = screen.getByTestId("app-content");

    expect(header).toBeInTheDocument();
    expect(nav).toBeInTheDocument();
    expect(content).toBeInTheDocument();
  });
});
