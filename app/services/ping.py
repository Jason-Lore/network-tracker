import asyncio
import platform

from datetime import datetime, timezone
from bson import ObjectId
from app.database import db


async def ping_ip(ip_address: str) -> bool:

    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", ip_address]
    else:
        command = ["ping", "-c", "1", "-W", "2", ip_address]

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )

    await process.communicate()

    return process.returncode == 0


async def ping_ip_five_times(ip_address: str):

    success_count = 0

    for _ in range(5):

        if await ping_ip(ip_address):
            success_count += 1

    is_online = success_count > 0

    return is_online, success_count


async def check_one_device(device_id: str):

    device = await db.devices.find_one({
        "_id": ObjectId(device_id)
    })

    if not device:
        return None

    ip_address = device.get("ip_address")

    if not ip_address:
        return None

    is_online, success_count = await ping_ip_five_times(ip_address)

    status_update = {
        "is_online": is_online,
        "last_checked": datetime.now(timezone.utc).isoformat(),
        "ping_success_count": success_count
    }

    await db.devices.update_one(
        {"_id": device["_id"]},
        {"$set": status_update}
    )

    return status_update


async def check_all_devices():

    devices = await db.devices.find().to_list(length=1000)

    for device in devices:

        await check_one_device(str(device["_id"]))


async def ping_loop():

    while True:

        print("Running scheduled device checks...")

        await check_all_devices()

        print("Scheduled device checks complete.")

        await asyncio.sleep(300)