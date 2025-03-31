import React from "react";



export const defaultTemplate = (mainElement: React.JSX.Element, nav_blog: React.JSX.Element) => (<>
    {nav_blog}
    <div className="container-fluid mb-3 mt-2 d-flex justify-content-center" id='main-page'>
        <div className="row w-100 justify-content-center">
            {mainElement}
        </div>
    </div>
</>);