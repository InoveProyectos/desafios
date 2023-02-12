#!/usr/bin/env python

import os
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

PORT = int(os.environ.get("PORT", 9000))

MONGO = {
    "uri": os.environ.get("MONGO_URI", "mongodb://localhost:27017"),
}
