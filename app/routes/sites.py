from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.database import db
from app.models.site import Site
from app.utils import format_site

router = APIRouter(
    prefix="/sites",
    tags=["Sites"]
)

# GET ROUTES
@router.get("/", response_model=list[Site])
async def get_sites():
    try:
        sites = await db.sites.find().to_list(length=100)
        formatted_sites = [format_site(s) for s in sites]
        return formatted_sites
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error fetching sites: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )

@router.get("/{site_id}", response_model=Site)
async def get_site(site_id: str):
    try:
        site = await db.sites.find_one({"_id": ObjectId(site_id)})
        if site:
            return format_site(site)
        else:
            raise HTTPException(status_code=404, detail="Site not found")
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error fetching site: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )

# POST ROUTES

@router.post("/")
async def create_site(site: Site):

    try: 
        site_dict = site.model_dump(exclude={"id"})

        result = await db.sites.insert_one(site_dict)
        return {
            "message": "Site created successfully",
            "site_id": str(result.inserted_id)
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error inserting site: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )


# DELETE ROUTES

@router.delete("/{site_id}")
async def delete_site(site_id: str):
    try:
        result = await db.sites.delete_one({"_id": ObjectId(site_id)})
        if result.deleted_count == 1:
            return {"message": "Site deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Site not found")
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error deleting site: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )

# PUT ROUTES

@router.put("/{site_id}")
async def update_site(site_id: str, site: Site):
    try:
        site_dict = site.model_dump(exclude={"id"})
        result = await db.sites.update_one(
            {"_id": ObjectId(site_id)},
            {"$set": site_dict}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Site not found")
            return {"message": "Site updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error updating site: {e}")
        raise HTTPException(
            status_code=500, 
            detail=str(e),
        )