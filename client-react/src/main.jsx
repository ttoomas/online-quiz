import { createRoot } from 'react-dom/client'
import App from './App.jsx'

import "primereact/resources/themes/saga-blue/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";

createRoot(document.getElementById('root')).render(
  <App />
)
