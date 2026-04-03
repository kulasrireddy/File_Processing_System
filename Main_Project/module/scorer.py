from module.loader import tokenize, clean_text

positive_words = {
    "good","great","excellent","amazing","love","nice","happy",
    "fast","best","awesome","perfect","satisfied","fantastic",
    "wonderful","super","quality","recommend","liked","awesome"
}

negative_words = {
    "bad","poor","terrible","worst","hate","angry",
    "slow","delay","broken","damaged","disappointed","problem",
    "waste","useless","cheap","defective","not working","issue"
}

intensifiers = {"very","extremely","really","too","highly","super"}

spam_words = {"spam","offer","buy now","promotion","congratulations","won"}
scam_words = {"scam","fraud","fake","cheated"}
sarcasm_words = {"yeah right","as if","wow great not","sure great"}


def calculate_score(text):
    words = tokenize(text)
    score = 0
    multiplier = 1

    for w in words:
        if w in intensifiers:
            multiplier = 2
            continue

        if w in positive_words:
            score += 2 * multiplier
            multiplier = 1

        elif w in negative_words:
            score -= 2 * multiplier
            multiplier = 1

    return score


def classify_sentiment(score, text):
    text = text.lower()

    if any(w in text for w in scam_words):
        return "Scam"
    if any(w in text for w in spam_words):
        return "Spam"
    if any(w in text for w in sarcasm_words):
        return "Sarcasm"

    if score >= 3:
        return "Strong Positive"
    elif score > 0:
        return "Positive"
    elif score == 0:
        return "Neutral"
    elif score <= -3:
        return "Strong Negative"
    else:
        return "Negative"


def classify_category(text):
    text = text.lower()

    if "refund" in text or "return" in text:
        return "Refund"
    elif "late" in text or "delivery" in text:
        return "Delivery"
    elif "broken" in text or "damaged" in text:
        return "Damage"
    elif "rude" in text or "support" in text:
        return "Service"
    elif "expensive" in text or "price" in text:
        return "Price"
    else:
        return "General"


def process_batch(batch):
    results = []

    for line in batch:
        if line.strip():
            clean = clean_text(line)

            score = calculate_score(clean)
            sentiment = classify_sentiment(score, clean)
            category = classify_category(clean)

            results.append((clean, score, sentiment, category))

    return results