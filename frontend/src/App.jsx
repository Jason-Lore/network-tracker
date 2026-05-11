import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import "leaflet/dist/leaflet.css";

import Sites from "./pages/Sites";
import SiteDetail from "./pages/SiteDetail";
import AddDevice from "./pages/AddDevice";
import AddSite from "./pages/AddSite";

function App() {

  return (
    <>
    <h1>
      <a href="/">Network Tracker</a>
    </h1>
    <div>
      <a href="/add-device">Add Device</a>
      <a href="/add-site">Add Site</a>
    </div>
      <BrowserRouter>
        <Routes>

          <Route path="/" element={<Sites />} />

          <Route
            path="/sites/:siteId"
            element={<SiteDetail />}
          />

          <Route
            path="/add-device"
            element={<AddDevice />}
          />

          <Route
            path="/add-site"
            element={<AddSite />}
          />

        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;