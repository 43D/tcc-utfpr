import React from "react";
import ReactDOM from 'react-dom/client'
import { RouterProvider } from "react-router-dom";
import { RoutesApp } from "./routes/routes";
import { pywebview } from "./type/pywebview/index.d";
import './index.css'

declare global {
  interface Window {
      pywebview: pywebview;
  }
}

const routes = RoutesApp();

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={routes} />
  </React.StrictMode>
)
