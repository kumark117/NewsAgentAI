from collections import Counter


def score_topics(topics, weights):

    topic_counts = Counter(topics)

    topic_scores = {}

    for topic, count in topic_counts.items():

        score = (
            weights.get("frequency",1)*count +
            weights.get("growth",1)*count +
            weights.get("spread",1)*count +
            weights.get("persistence",1)*count
        )

        topic_scores[topic] = score

    return topic_scores