export const UnsupportedIndex = () => (<>
    <div className="d-flex flex-column align-items-center justify-content-center w-100" style={{ height: "calc( 100vh - 120px )" }}>
        <div className="spinner-border" role="status" style={{ height: "40vh", width: "40vh", fontSize: "50pt" }}>
            <span className="visually-hidden">Carregando...</span>
        </div>
        <h4 className="mb-0 mt-4">Carregando...</h4>
    </div>

    <div className="d-flex flex-column align-items-center justify-content-end mt-5 w-100">
        <p className="mb-0">PySocial náo possui suporte fora do aplicarivo!</p>
        <p style={{ color: `blue`, cursor: "pointer" }} onClick={() => window.location.reload()}>Clique aqui para recarregar essa página</p>
    </div>
</>);
