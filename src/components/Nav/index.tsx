import './index.css';

const Nav = () => {

    return (
        <>
            <nav className="navbar navbar-expand-lg sticky-top" style={{ backgroundColor: "#103b47" }}>
                <div className="container-fluid mx-5" >
                    <div className="w-100 mx-5">
                        <form className="d-flex mx-5" role="modal">
                            <input className="form-control" type="search" placeholder="Escreva algo..." aria-label="open" disabled />
                        </form>
                    </div>
                    <div className="d-flex align-items-center">
                        <button className="btn btn-primary mx-2" style={{minWidth: "150px"}}>Adicionar conta</button>
                        <button className="btn btn-primary me-2"><i className="bi bi-gear"></i></button>
                    </div>
                </div>
            </nav>
        </>
    )
}

export default Nav