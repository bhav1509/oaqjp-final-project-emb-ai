import requests

def emotion_detector(text_to_analyze):

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id":"emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input, headers=headers)
    formatted_response = response.json()
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    if anger == max(anger, disgust, fear, joy, sadness):
        dominant_emotion = "anger"
    elif disgust == max(anger, disgust, fear, joy, sadness):
        dominant_emotion = "disgust"
    elif fear == max(anger, disgust, fear, joy, sadness):
        dominant_emotion = "fear"
    elif joy == max(anger, disgust, fear, joy, sadness):
        dominant_emotion = "joy"

    else:
        dominant_emotion = "sadness"

    responsedict = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }

    return responsedict