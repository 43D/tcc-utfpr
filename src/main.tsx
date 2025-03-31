import { createRoot } from 'react-dom/client'
import { pywebview } from "./type/pywebview/index.d";
import './index.css'
import { App } from "./app";

declare global {
  interface Window {
    pywebview: pywebview;
  }
}

createRoot(document.getElementById('root')!)
  .render(<>
    <App />
  </>
  )
