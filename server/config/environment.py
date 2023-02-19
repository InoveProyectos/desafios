#!/usr/bin/env python

import os
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

port = int(os.environ.get("PORT", 9000))

mongo = {
    "uri": os.environ.get("MONGO_URI", "mongodb://localhost:27017/challenges-dev"),
}

worker = {
    "url" : os.environ.get("WORKER_URL", "http://localhost:9001"),
}
