from fastapi import APIRouter, HTTPException

from app.db.repositories.soursec import create_source, get_all_sources, get_source_by_url, update_source_status, \
    delete_source
from app.models.sourse import Source

router = APIRouter(prefix='/sources', tags=['Sources'])

@router.post('', status_code=201)
async def add_sources(source: Source):
    source_result = await create_source(source)
    if source_result:
        return {'id': str(source_result)}
    else:
        raise HTTPException(status_code=409, detail="Source already exists")

@router.get('', status_code=200)
async def list_sources():
    sources_data = await get_all_sources()
    for data in sources_data:
        data['_id'] = str(data['_id'])

    return sources_data

@router.get('/by-url', status_code=200)
async def source_by_url(url: str):
    source_result = await get_source_by_url(url)
    if not source_result:
        raise HTTPException(status_code=404, detail="Source not found")
    source_result['_id'] = str(source_result['_id'])
    return source_result

@router.patch('/status', status_code=200)
async def update_source(url: str, is_active: bool):
    check_source = await get_source_by_url(url)
    if not check_source:
        raise HTTPException(status_code=404, detail="Source not found")

    await update_source_status(url, is_active)

    return {'message': 'updated source successfully'}

@router.delete('', status_code=200)
async def delete_sources(url: str):
    delete_count = await delete_source(url)

    if delete_count == 0:
        raise HTTPException(status_code=404, detail="Source not found")

    return {'message': 'deleted source successfully'}
