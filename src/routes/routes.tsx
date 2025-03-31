import { createBrowserRouter } from "react-router-dom";
import { defaultTemplate } from "../template/defaultTemplate";
import { MainPageIndex } from "../components";
import { PywebviewApiType } from "../type/pywebview/index.d";
import { UnsupportedIndex } from "../components/unsupported";

export const RoutesApp = (pyApi: PywebviewApiType, nav_blog: React.JSX.Element) => {

  const routes = createBrowserRouter([
    {
      path: '/*',
      element: defaultTemplate(<MainPageIndex pyApi={pyApi} />, nav_blog)
    }
  ]);

  return routes;
}

export const RoutesAppUnsupported = () => {

  const routes = createBrowserRouter([
    {
      path: '/*',
      element: <UnsupportedIndex />
    }
  ]);

  return routes;
}