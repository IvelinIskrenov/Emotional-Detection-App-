import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion in a given text locally.
    """
    
    if not text_to_analyze:
        return None

    text_lower = text_to_analyze.lower()
    
    keywords = {
        'anger': ['angry', 'hate', 'mad', 'rage', 'furious', 'stupid', 'idiot', 'bad'],
        'joy': ['happy', 'joy', 'love', 'wonderful', 'great', 'fun', 'smile', 'good'],
        'fear': ['scared', 'fear', 'afraid', 'terrified', 'horror', 'danger'],
        'sadness': ['sad', 'crying', 'unhappy', 'depressed', 'grief', 'tears', 'sorry'],
        'disgust': ['yuck', 'disgusting', 'gross', 'nasty', 'awful', 'sick']
    }

    scores = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0
    }

    words = text_lower.split()
    total_matches = 0

    for word in words:
        for emotion, emotion_words in keywords.items():
            if word in emotion_words:
                scores[emotion] += 1.0
                total_matches += 1

    if total_matches == 0:
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'neutral'
        }

    for emotion in scores:
        scores[emotion] = scores[emotion] / total_matches

    dominant_emotion = max(scores, key=scores.get)
    scores['dominant_emotion'] = dominant_emotion

    return scores