from collections import defaultdict

topic_memory = defaultdict(lambda: {
    "history": [],
    "alpha": 1,
    "beta": 1
})