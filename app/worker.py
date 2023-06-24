from app.repositories.mongo.strip_repo import StripRepositoryMongo
from app.service.utils import func_logger


@func_logger()
async def create_strip_records(post):
    repo = StripRepositoryMongo()
    await repo.create_records(post)
