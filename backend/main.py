from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from feeds import fetch_topics
from scorer import score_topics

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/trends")
def trends():
    topics = fetch_topics()
    return score_topics(topics)