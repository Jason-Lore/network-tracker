import { useEffect, useState } from "react";

function AddDevice() {

  const [sites, setSites] = useState([]);

  useEffect(() => {

    fetch("http://192.168.0.49:8000/sites")
      .then(res => res.json())
      .then(data => {
        setSites(data);
      });

  }, []);

  const submitForm = async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);

    const newDevice = {
      device_name: formData.get("device_name"),
      ip_address: formData.get("ip_address"),
      site_id: formData.get("site"),
      device_type: formData.get("device_type"),
      rack_location: formData.get("rack_location") || "",
      unit_location: formData.get("unit_location") || "",
      floor: formData.get("floor") || "",
      closet: formData.get("closet") || "",
      cabinet: formData.get("cabinet") || ""
    };

    const res = await fetch("http://192.168.0.49:8000/devices", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newDevice)
    });

    const data = await res.json();

    if (!res.ok) {
      console.error(data);
      alert("Failed to add device");
      return;
    }

    alert("Device added successfully");
    e.target.reset();
  };


  return (
    <div>
      <h1>Add Device</h1>
      <p>This is where you can add a new device to the system.</p>
      <form onSubmit={submitForm}>

        <label htmlFor="device_name">Device Name:</label>
        <input type="text" id="device_name" name="device_name" />

        <label htmlFor="ip_address">IP Address:</label>
        <input type="text" id="ip_address" name="ip_address" />

        <label htmlFor="site">Site:</label>
        <select id="site" name="site">
          {sites.map(site => (
            <option key={site.id} value={site.id}>
              {site.site_name}
            </option>
          ))}
        </select>

        <label htmlFor="device_type">Device Type:</label>
        <input type="text" id="device_type" name="device_type" />

        <label htmlFor="rack_location">Rack Location:</label>
        <input type="text" id="rack_location" name="rack_location" />

        <label htmlFor="unit_location">Unit Location:</label>
        <input type="text" id="unit_location" name="unit_location" />

        <label htmlFor="floor">Floor:</label>
        <input type="text" id="floor" name="floor" />

        <label htmlFor="closet">Closet:</label>
        <input type="text" id="closet" name="closet" />

        <label htmlFor="cabinet">Cabinet:</label>
        <input type="text" id="cabinet" name="cabinet" />

        <button type="submit">Add Device</button>
      </form>

    </div>
  );
}

export default AddDevice;