import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function SiteDetail() {

  const { siteId } = useParams();

  const [devices, setDevices] = useState([]);

  useEffect(() => {

    fetch(`http://192.168.0.49:8000/sites/${siteId}/devices`)
      .then(res => res.json())
      .then(data => {
        setDevices(data);
      });

  }, [siteId]);

  return (
    <div>

      <h1>Devices</h1>

      {devices.map(device => (
        <div key={device.id}>
          <h2>{device.device_name}</h2>
          <p>{device.ip_address}</p>
          <p>{device.is_online ? "🟢" : "🔴"}</p>
        </div>
      ))}

    </div>
  );
}

export default SiteDetail;