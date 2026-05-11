from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.database import db
from app.models.device import Device
from app.utils import format_device
from app.routes import sites, devices

router = APIRouter(tags=["Devices"])

@router.get("/devices", response_model=list[Device])
async def get_devices():
    try:
        devices = await db.devices.find().to_list(length=100)
        formatted_devices = [format_device(d) for d in devices]
        return formatted_devices
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error fetching devices: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )

@router.get("/sites/{site_id}/devices", response_model=list[Device])
async def get_devices_by_site(site_id: str):
    try:
        devices = await db.devices.find({"site_id": ObjectId(site_id)}).to_list(length=100)
        formatted_devices = [format_device(d) for d in devices]
        return formatted_devices
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error fetching devices for site {site_id}: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@router.get("/devices/{device_id}", response_model=Device)
async def get_device(device_id: str):
    try:
        device = await db.devices.find_one({"_id": ObjectId(device_id)})
        if device:
            return format_device(device)
        else:
            raise HTTPException(status_code=404, detail="Device not found")
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error fetching device: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )

# POST endpoints

@router.post("/devices")
async def create_device(device: Device):
    try:
        device_dict = device.model_dump(exclude={"id"})

        device_dict["site_id"] = ObjectId(device.site_id)

        result = await db.devices.insert_one(device_dict)
        return {
            "message": "Device created successfully",
            "device_id": str(result.inserted_id)
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error inserting device: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

#DELETE endpoints

@router.delete("/devices/{device_id}")
async def delete_device(device_id: str):
    try:
        result = await db.devices.delete_one({"_id": ObjectId(device_id)})
        if result.deleted_count == 1:
            return {"message": "Device deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Device not found")
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error deleting device: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )

#PUT endpoints

@router.put("/devices/{device_id}")
async def update_device(device_id: str, device: Device):
    try:
        device_dict = device.model_dump(exclude={"id"})
        device_dict["site_id"] = ObjectId(device.site_id)
        result = await db.devices.update_one(
            {"_id": ObjectId(device_id)},
            {"$set": device_dict}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Device not found")
            return {"message": "Device updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error updating device: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )