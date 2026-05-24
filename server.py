''' Server module for emotion detection'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    ''' Method for emotion detection of entered text'''
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response "
    f"is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, "
    f"'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    ''' method to render index page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)
