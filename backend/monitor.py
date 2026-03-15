import time
from feeds import fetch_topics
from scorer import score_topics

print("NewsAgent monitoring started...")

while True:

    topics = fetch_topics()
    results = score_topics(topics)

    print("\nTop Trends:")

    for r in results["trends"]:
        print(r["topic"], "| trend:", r["trend_score"])

    print("\nSpike Alerts:")

    for r in results["spikes"]:
        print(r["topic"], "| spike:", r["spike_score"])

    print("-----")

    time.sleep(60)