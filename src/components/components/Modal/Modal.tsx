type Props = {
    id: string;
    title: string;
    contentElement: JSX.Element;
}

export function ModalTemplate({ id, title, contentElement }: Props) {

    return (
        <>
            <div className="modal fade" id={id} data-bs-backdrop="static" data-bs-keyboard="false" tabIndex={-1} aria-labelledby={`${id}-label`} aria-hidden="true">
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h1 className="modal-title fs-5" id={`${id}-label`}>{title}</h1>
                            <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div className="modal-body">
                            {contentElement}
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}