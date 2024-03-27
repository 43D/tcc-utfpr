import { useNavigate } from "react-router-dom";


const NotFound = () => {
    const navigate = useNavigate();

    return (
        <div className="d-flex justify-content-center align-items-center flex-column" style={{ minHeight: "75vh" }}>
            <h4 className="text-center mb-1">Error 404</h4>
            <p className="text-center"><span className="text-danger fw-bold" onClick={() => navigate(-1)} style={{ cursor: "pointer" }}>Clique aqui</span> para voltar...</p>
        </div>
    );
}

export default NotFound