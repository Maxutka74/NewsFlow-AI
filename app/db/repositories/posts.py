from bson import ObjectId

from app.db.mongodb import db
from app.models.post import Post


async def create_post(post: Post):
    data = post.model_dump()
    result = await db['posts'].insert_one(data)
    return result.inserted_id

async def get_post_by_id(post_id: str):
    return await db['posts'].find_one({'_id': ObjectId(post_id)})

async def update_post_status(post_id: str, status: str):
    updated_post = await db['posts'].update_one({'_id': ObjectId(post_id)},
                                        {'$set': {'status': status}}
                                        )
    return updated_post.modified_count