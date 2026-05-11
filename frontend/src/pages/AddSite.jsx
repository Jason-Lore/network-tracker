import { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, useMap, useMapEvents } from "react-leaflet";

function MapUpdater({ markerPosition }) {
    const map = useMap();

    useEffect(() => {
        if (markerPosition) {
            map.setView(markerPosition, 16);
        }
    }, [markerPosition, map]);

    return null;
}

function LocationPicker({ setLatitude, setLongitude, setMarkerPosition, reverseGeocode, markerPosition }) {
    useMapEvents({
        click(e) {
            const { lat, lng } = e.latlng;

            setLatitude(lat);
            setLongitude(lng);
            setMarkerPosition([lat, lng]);

            reverseGeocode(lat, lng);
        }
    });

    return markerPosition ? <Marker position={markerPosition} /> : null;
}

function AddSite() {
    const [address, setAddress] = useState("");
    const [latitude, setLatitude] = useState("");
    const [longitude, setLongitude] = useState("");
    const [markerPosition, setMarkerPosition] = useState(null);

    const reverseGeocode = async (lat, lon) => {
        const url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lon}`;

        const res = await fetch(url);
        const data = await res.json();

        if (data?.display_name) {
            setAddress(data.display_name);
        }
    };

    const forwardGeocode = async () => {
        if (!address.trim()) return;

        const url = `https://nominatim.openstreetmap.org/search?format=jsonv2&q=${encodeURIComponent(address)}&limit=1`;

        const res = await fetch(url);
        const data = await res.json();

        if (data.length > 0) {
            const result = data[0];

            const lat = Number(result.lat);
            const lon = Number(result.lon);

            setLatitude(lat);
            setLongitude(lon);
            setAddress(result.display_name);
            setMarkerPosition([lat, lon]);
        }
    };

    const submitForm = async (e) => {
        e.preventDefault();

        const formData = new FormData(e.target);

        const newSite = {
            site_name: formData.get("site_name"),
            address: formData.get("address"),
            latitude: Number(latitude),
            longitude: Number(longitude)
        };

        const res = await fetch("http://192.168.0.49:8000/sites", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(newSite)
        });

        if (!res.ok) {
            alert("Failed to add site");
            return;
        }

        alert("Site added successfully");
        e.target.reset();
        setLatitude("");
        setLongitude("");
        setMarkerPosition(null);
    };

    return (
        <div>
            <h1>Add Site</h1>

            <form onSubmit={submitForm}>
                <label htmlFor="site_name">Site Name:</label>
                <input type="text" id="site_name" name="site_name" />

                <input
                    type="text"
                    id="address"
                    name="address"
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                />

                <button type="button" onClick={forwardGeocode}>
                    Find Address
                </button>

                <label htmlFor="latitude">Latitude:</label>
                <input
                    type="number"
                    step="any"
                    id="latitude"
                    name="latitude"
                    value={latitude}
                    onChange={(e) => setLatitude(e.target.value)}
                />

                <label htmlFor="longitude">Longitude:</label>
                <input
                    type="number"
                    step="any"
                    id="longitude"
                    name="longitude"
                    value={longitude}
                    onChange={(e) => setLongitude(e.target.value)}
                />

                <div style={{ height: "400px", width: "100%", marginTop: "20px" }}>
                    <MapContainer
                        center={[45.5152, -122.6784]}
                        zoom={12}
                        style={{ height: "100%", width: "100%" }}
                    >
                        <TileLayer
                            attribution="&copy; OpenStreetMap contributors"
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />

                        <LocationPicker
                            setLatitude={setLatitude}
                            setLongitude={setLongitude}
                            setMarkerPosition={setMarkerPosition}
                            reverseGeocode={reverseGeocode}
                            markerPosition={markerPosition}
                        />
                        <MapUpdater markerPosition={markerPosition} />
                    </MapContainer>
                </div>

                <button type="submit">Add Site</button>
            </form>
        </div>
    );
}

export default AddSite;