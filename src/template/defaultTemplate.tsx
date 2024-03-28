import { Nav } from "../components/Nav";



export const defaultTemplate = (mainElement: JSX.Element) => {
    const nav_blog = <Nav />;

    return (<>
        {nav_blog}
        <div className="container-fluid mb-3 mt-2 d-flex justify-content-center" id='main-page'>
            <div className="row w-100 justify-content-center">
                {mainElement}
            </div>
        </div>
    </>)
}