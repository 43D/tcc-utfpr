import './index.css';

export function Nav() {

    return (
        <>
            <nav className="navbar navbar-expand-lg sticky-top" style={{ backgroundColor: "#103b47" }}>
                <div className="container-fluid" >
                    <div className="col-5 col-sm-8 col-lg-9 justify-content-center d-flex">
                        <button className='btn btn-light w-50 text-start rounded-pill' data-bs-toggle="modal" data-bs-target="#post-modal">Escreva algo...</button>
                    </div>
                    <div className="col d-flex align-items-center justify-content-end">
                        <button className="btn btn-primary mx-2" style={{ minWidth: "150px" }} data-bs-toggle="modal" data-bs-target="#add-account">Adicionar conta</button>
                        <button className="btn btn-primary me-2" data-bs-toggle="modal" data-bs-target="#settings"><i className="bi bi-gear"></i></button>
                    </div>
                </div>
            </nav>
        </>
    )
}