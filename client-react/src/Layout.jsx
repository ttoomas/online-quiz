import "primereact/resources/themes/saga-blue/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";


export default function ({ children }) {
    return (
        <div>
            <header>{/* Header content goes here */}</header>

            <main>{children}</main>

            <footer>{/* Footer content goes here */}</footer>
        </div>
    );
}
