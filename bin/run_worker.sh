#!/bin/sh

set -ev

echo " WORKER STARTED..."
rq worker --connection-class app.controllers.redis.RedisConnection  post_queue