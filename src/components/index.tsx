import { PywebviewApiType } from '../type/pywebview/index.d';
import { ModalTemplate } from './components/Modal/Modal';
import { TestPage } from './components/test';

type props = {
  pyApi: PywebviewApiType;
}

export const MainPageIndex = ({ pyApi }: props) => {
  pyApi;

  return (
    <>
      <div className="col-9">
        main
      </div>
      <div className="col">
        aside
      </div>
      <ModalTemplate id='post-modal' title='Criar uma nova postagem...' contentElement={<TestPage />} />
      <ModalTemplate id='add-account' title='Adicionar uma nova conta...' contentElement={<TestPage />} />
      <ModalTemplate id='settings' title='Configurações' contentElement={<TestPage />} />
    </>
  )
}