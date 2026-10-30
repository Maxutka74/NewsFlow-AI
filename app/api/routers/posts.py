from typing import Literal

from bson import ObjectId
from fastapi import APIRouter, HTTPException

from app.db.repositories.posts import get_post_by_id, update_post_status

router = APIRouter(prefix='/posts', tags=['Posts'])

@router.get('/{post_id}')
async def post(post_id: str):
    if not ObjectId.is_valid(post_id):
        raise HTTPException(
            status_code=400,
            detail='Invalid post ID'
        )

    post_result = await get_post_by_id(post_id)

    if not post_result:
        raise HTTPException(status_code=404, detail='Post not found')

    post_result['_id'] = str(post_result['_id'])
    return post_result

@router.patch('/{post_id}/status')
async def change_post_status(post_id: str, status: Literal['pending', 'approved', 'rejected', 'published']):
    if not ObjectId.is_valid(post_id):
        raise HTTPException(
            status_code=400,
            detail='Invalid post ID'
        )
    post_result = await get_post_by_id(post_id)

    if not post_result:
        raise HTTPException(status_code=404, detail='Post not found')

    await update_post_status(post_id, status)

    return {'message': 'Post status updated successfully'}