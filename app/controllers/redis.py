from redis import Redis
from app.settings import REDIS_HOST, REDIS_PORT, REDIS_DB
from rq import Queue
from app.constants import REDIS_TASK_NAME
from app.worker import create_strip_records


class RedisConnection(Redis):

    def __init__(
        self,
        host,
        port,
        db,
        password=None,
        ssl=None,
        ssl_ca_certs=None,
        ssl_cert_reqs=None
    ):
        super().__init__(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=password,
            ssl=ssl,
            ssl_ca_certs=ssl_ca_certs,
            ssl_cert_reqs=ssl_cert_reqs,
        )


async def enqueue_post(post):

    redis_connection = RedisConnection(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
    )
    queue = Queue(REDIS_TASK_NAME, connection=redis_connection)

    queue.enqueue(create_strip_records, post)
