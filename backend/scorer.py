from topic_memory import topic_memory
from growth import growth_score
from persistence import persistence_score
from acceleration import acceleration_score
from confidence import confidence

from fold import fold_topics
from learner import load_weights, save_weights, adjust_weights


def score_topics(topics):

    clusters = fold_topics(topics)

    weights = load_weights()

    results = []

    for c in clusters:

        topic = c["title"]
        count = c["count"]

        mem = topic_memory[topic]
        mem["history"].append(count)

        history = mem["history"]

        g = growth_score(history)
        p = persistence_score(history)
        a = acceleration_score(history)

        trend_score = (
            weights["frequency"] * count +
            weights["persistence"] * p +
            weights["growth"] * g
        )

        spike_score = 0

        if count >= 2 and g > 0 and a > 0:
            spike_score = a * count

        conf = confidence(mem)

        results.append({
            "topic": topic,
            "trend_score": round(trend_score,3),
            "spike_score": round(spike_score,3),
            "confidence": round(conf,3)
        })

    trends = sorted(results, key=lambda x: x["trend_score"], reverse=True)[:5]

    spikes = sorted(results, key=lambda x: x["spike_score"], reverse=True)[:3]

    weights = adjust_weights(results, weights)
    save_weights(weights)

    return {
        "trends": trends,
        "spikes": spikes
    }