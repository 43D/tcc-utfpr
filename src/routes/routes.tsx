import { createBrowserRouter } from "react-router-dom";
import NotFound from "../components/NotFound";
import MainPage from "../components";
import { defaultTemplate } from "../template/defaultTemplate";

export const RoutesApp = () => {
  const routes = createBrowserRouter([
    {
      path: '/',
      element: defaultTemplate(<MainPage />),
    },
    {
      path: '/404',
      element: defaultTemplate(<NotFound />),
    },
    {
      path: '/*',
      element: defaultTemplate(<NotFound />),
    },
  ]);

  return routes;
}