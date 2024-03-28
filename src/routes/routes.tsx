import { createBrowserRouter } from "react-router-dom";
import { defaultTemplate } from "../template/defaultTemplate";
import { MainPageIndex } from "../components";

export const RoutesApp = () => {
  const routes = createBrowserRouter([
    {
      path: '/*',
      element: defaultTemplate(<MainPageIndex />),
    },
  ]);

  return routes;
}