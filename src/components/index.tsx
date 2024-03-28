import { ModalTemplate } from './components/Modal/Modal';
import TestPage from './components/test';

export function MainPageIndex() {

  return (
    <>
      <div className="col-9">
        main
      </div>
      <div className="col">
        aside
      </div>
      <ModalTemplate id='teste' contentElement={<TestPage />} />
    </>
  )
}