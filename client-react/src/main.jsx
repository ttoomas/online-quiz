import { createRoot } from 'react-dom/client'
import App from './App.jsx'

import { Provider } from "react-redux";
import store from "./Helpers/redux/store.js";

import "primereact/resources/themes/saga-blue/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";

createRoot(document.getElementById('root')).render(
  <Provider store={store}>
    <App />
  </Provider>
)
