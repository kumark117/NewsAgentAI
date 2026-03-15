import time
import json
import os
import datetime

from feeds import fetch_topics
from scorer import score_topics
from learner import load_weights

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_PATH = os.path.join(DATA_DIR, "results.json")


def save_results(trends, spikes, cycle):

    os.makedirs(DATA_DIR, exist_ok=True)

    payload = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "cycle": cycle,
        "trends": trends,
        "spikes": spikes
    }

    with open(RESULTS_PATH, "w") as f:
        json.dump(payload, f, indent=2)


def run_agent():

    print("AI News Trend Agent started")

    cycle = 0

    while True:

        cycle += 1
        print(f"\nAgent cycle {cycle}")

        try:

            topics = fetch_topics()

            topic_scores = score_topics(topics, load_weights())

            previous_scores = {}
            spikes = []
            trends = []

            for topic, score in topic_scores.items():

                prev = previous_scores.get(topic, 0)
                delta = score - prev

                previous_scores[topic] = score

            obj = {
                "topic": topic,
                "score": score
            }

            if delta >= 2:      # demo-friendly threshold
                spikes.append(obj)
            else:
                trends.append(obj)

            save_results(trends, spikes, cycle)

            print("Results updated")

        except Exception as e:

            print("Agent error:", e)

        time.sleep(30)


if __name__ == "__main__":
    run_agent()
