#!/usr/bin/env python

import os
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

port = int(os.environ.get("PORT", 9000))

connections = {
    "mongo": {
        "uri": os.environ.get("MONGO_URI", "mongodb://localhost:27017/challenges-dev")
    },
    "redis": {
        "host": os.environ.get("REDIS_URI", "localhost"),
        "port": os.environ.get("REDIS_PORT", 6379),
        "password": os.environ.get("REDIS_PASSWORD", "perritobarrios"),
        "ttl": int(os.environ.get("REDIS_TTL", 60 * 60 * 2)) # 2 hours
        "db": int(os.environ.get("REDIS_DB", 0))
    }
}

workers = {
    "pyworker" : {
        "url": os.environ.get("WORKER_URL", "http://localhost:9001")
    }
}
