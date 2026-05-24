Final project

# NLP Emotion Detection Web Application

<img width="1280" height="756" alt="6b_deployment_test" src="https://github.com/user-attachments/assets/bc3e45f4-706c-47d8-8703-7b8fd1d7e0d9" />

This project is a Flask-based NLP Emotion Detection application that analyzes user-provided text and identifies emotions using IBM Watson NLP APIs.

The application accepts text input from the user through a web interface, sends the text to the Watson Emotion Prediction API, processes the response, and displays:

- Anger
- Disgust
- Fear
- Joy
- Sadness
- Dominant Emotion

---

## Features Implemented

- Emotion analysis using IBM Watson NLP API
- Flask web application deployment on localhost:5000
- REST endpoint using `/emotionDetector`
- Emotion score extraction and dominant emotion detection
- Error handling for blank inputs
- Unit testing for emotion detection functionality
- Modular package structure using `EmotionDetection`
- Pylint-compliant code improvements

---

## Technologies Used

- Python
- Flask
- Requests Library
- IBM Watson NLP API
- UnitTest
- Pylint

---

## Project Structure

```text 
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
└── README.md
```
---

## Example Output

### Input

```text

I think I am having fun

```

### Output

```text

For the given statement, the system response is 

'anger': 0.029103195, 

'disgust': 0.0067921067, 

'fear': 0.027528232, 

'joy': 0.876574 and 

'sadness': 0.06151191. 

The dominant emotion is joy.

```

---

## Error Handling

The application gracefully handles blank user input.

If the user submits an empty input, the system displays:

```text

Invalid text! Please try again!

```

This was implemented using:

- API response validation

- `None` checks for dominant emotion

- Flask route-level validation

---

## Deployment

The Flask application is deployed locally using:

```bash

python3 server.py

```

The application runs on:

```text

http://localhost:5000

```

---

## Outputs:

<img width="1280" height="756" alt="6b_deployment_test" src="https://github.com/user-attachments/assets/bc3e45f4-706c-47d8-8703-7b8fd1d7e0d9" />

<img width="1280" height="756" alt="7c_error_handling_interface" src="https://github.com/user-attachments/assets/28591d34-d5b6-4195-8a9b-86f65abff850" />

## Assessment:

<img width="1280" height="712" alt="Screenshot 2026-05-24 at 4 37 28 PM" src="https://github.com/user-attachments/assets/0ceb13d5-53ff-4a3b-aec5-cf28b16f368b" />



