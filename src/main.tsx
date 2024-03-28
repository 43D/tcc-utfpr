import React from "react";
import ReactDOM from 'react-dom/client'
import { RouterProvider } from "react-router-dom";
import { RoutesApp } from "./routes/routes";
import { pywebview } from "./type/pywebview/index.d";
import { Api, ApiType } from "./infra/API/Api";
import './index.css'

declare global {
  interface Window {
      pywebview: pywebview;
      API: ApiType;
  }
}
window.API = Api();

const routes = RoutesApp();

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={routes} />
  </React.StrictMode>
)
