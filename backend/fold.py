import re

# words we ignore
STOP = {
    "the","a","an","and","or","with","for","to","of","in","on",
    "is","are","was","were","this","that","these","those"
}

# anchor entities commonly seen in tech news
ANCHORS = {
    "chatgpt","openai","tesla","apple","google","microsoft",
    "meta","facebook","amazon","nvidia","uber","spotify",
    "intel","amd","xai","musk","android","iphone","ipad"
}


def clean(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]','',text)
    return text


def words(text):
    text = clean(text)
    return [w for w in text.split() if w not in STOP]


def anchor_from_words(ws):

    # explicit anchors first
    for w in ws:
        if w in ANCHORS:
            return w

    # fallback: longest meaningful word
    ws = sorted(ws, key=len, reverse=True)

    for w in ws:
        if len(w) >= 5:
            return w

    return ws[0] if ws else None


def similarity(a,b):

    wa=set(words(a))
    wb=set(words(b))

    inter=len(wa & wb)
    union=len(wa | wb)

    if union==0:
        return 0

    return inter/union


def fold_topics(titles):

    clusters=[]

    for t in titles:

        ws = words(t)
        anchor = anchor_from_words(ws)

        matched=False

        for c in clusters:

            # anchor match (strong signal)
            if anchor and anchor in c["anchors"]:
                c["count"] += 1
                c["titles"].append(t)
                matched=True
                break

            # lexical similarity fallback
            if similarity(t,c["title"]) > 0.4:
                c["count"] += 1
                c["titles"].append(t)
                matched=True
                break


        if not matched:

            clusters.append({
                "title":t,
                "count":1,
                "anchors":{anchor} if anchor else set(),
                "titles":[t]
            })


    return clusters
