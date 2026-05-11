def format_device(device):
    return {
        "id": str(device["_id"]),
        "device_name": device["device_name"],
        "device_type": device["device_type"],
        "site_id": str(device["site_id"]),
        "rack_location": device.get("rack_location"),
        "unit_location": device.get("unit_location"),
        "floor": device.get("floor"),
        "closet": device.get("closet"),
        "cabinet": device.get("cabinet"),
        "ip_address": device.get("ip_address"),
        "is_online": device.get("is_online"),
        "last_checked": device.get("last_checked"),
        "ping_success_count": device.get("ping_success_count", 0)
    }

def format_site(site):
    return {
        "id": str(site["_id"]),
        "site_name": site["site_name"],
        "address": site["address"],
        "latitude": site["latitude"],
        "longitude": site["longitude"]
    }