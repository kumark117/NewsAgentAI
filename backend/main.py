from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import json
import os

from learner import load_weights

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(__file__)
RESULTS_PATH = os.path.join(BASE_DIR, "data", "results.json")


@app.get("/")
def home():
    return {"status": "AI News Agent running"}


@app.get("/trends")
def get_trends():

    if not os.path.exists(RESULTS_PATH):
        return {"trends": [], "spikes": []}

    with open(RESULTS_PATH) as f:
        return json.load(f)


@app.get("/weights")
def get_weights():
    return load_weights()