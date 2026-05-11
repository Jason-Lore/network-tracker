import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Sites() {

    const [sites, setSites] = useState([]);

    useEffect(() => {

        fetch("http://192.168.0.49:8000/sites")
            .then(res => res.json())
            .then(data => {
                setSites(data);
            });

    }, []);

    return (
        <div>
            {sites.map(site => (
                <div key={site.id}>
                    <Link to={`/sites/${site.id}`}>
                        {site.site_name}
                    </Link>
                    <p>{site.address}</p>
                </div>
            ))}
        </div>
    );
}

export default Sites;