import { RoutesApp, RoutesAppUnsupported } from "./routes/routes";
import { PyApi } from "./infra/core/pyApi";
import { useEffect, useState } from "react";
import { RouterProvider } from "react-router-dom";
import { NavIndex } from "./components/Nav";

export const App = () => {
    const unsupportedRoot = RoutesAppUnsupported();
    const nav_blog = <NavIndex />;
    const [routes, setRoutes] = useState<any>(undefined);
    const [pywebviewLoaded, setPywebviewLoaded] = useState<boolean>(false);
    
    useEffect(() => {
        const waitForPyWebView = (event: () => void) => {
            const interval = setInterval(() => {
                if (window.pywebview && window.pywebview.api) {
                    clearInterval(interval);
                    event();
                }
            }, 100); // Verifique a cada 100ms
        };
        waitForPyWebView(() => setPywebviewLoaded(true));
    }, []);

    useEffect(() => {
        if (!window.pywebview || !window.pywebview.api)
            return;
        const pyApi = PyApi(window.pywebview);
        setRoutes(RoutesApp(pyApi, nav_blog));
    }, [window.pywebview, pywebviewLoaded]);

    return (<>
        {(pywebviewLoaded && routes !== undefined) &&
            <RouterProvider router={routes} />
        }
        {(routes === undefined) &&
            <RouterProvider router={unsupportedRoot} />
        }
    </>
    )
}