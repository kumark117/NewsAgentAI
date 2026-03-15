from topic_memory import topic_memory
from growth import growth_score
from persistence import persistence_score
from acceleration import acceleration_score
from confidence import confidence

from fold import fold_topics
from learner import load_weights, save_weights, adjust_weights

def score_topics(topics):

    counts = {}
    clusters = fold_topics(topics)
    for t in clusters:
        counts[t] = counts.get(t,0) + 1

    results = []

    for topic,count in counts.items():

        mem = topic_memory[topic]
        mem["history"].append(count)

        history = mem["history"]

        g = growth_score(history)
        p = persistence_score(history)
        a = acceleration_score(history)

        trend_score = 0.5*count + 0.5*p
        spike_score = a

        conf = confidence(mem)

        results.append({
            "topic": topic,
            "trend_score": round(trend_score,3),
            "spike_score": round(spike_score,3),
            "confidence": round(conf,3)
        })

    trends = sorted(results, key=lambda x: x["trend_score"], reverse=True)[:5]

    spikes = sorted(results, key=lambda x: x["spike_score"], reverse=True)[:3]

    weights = load_weights()
    weights = adjust_weights(results, weights)
    save_weights(weights)

    return {
        "trends": trends,
        "spikes": spikes
    }