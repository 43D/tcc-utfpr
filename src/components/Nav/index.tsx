import './index.css';

export function Nav() {

    return (
        <>
            <nav className="navbar navbar-expand-lg sticky-top" style={{ backgroundColor: "#103b47" }}>
                <div className="container-fluid" >
                    <div className="col-5 col-sm-8 col-lg-9 justify-content-center d-flex">
                        <form className="d-flex w-50" role="modal">
                            <input className="form-control" type="search" placeholder="Escreva algo..." aria-label="open" disabled />
                        </form>
                    </div>
                    <div className="col d-flex align-items-center justify-content-end">
                        <button className="btn btn-primary mx-2" style={{ minWidth: "150px" }} data-bs-toggle="modal" data-bs-target="#teste">Adicionar conta</button>
                        <button className="btn btn-primary me-2"><i className="bi bi-gear"></i></button>
                    </div>
                </div>
            </nav>
        </>
    )
}