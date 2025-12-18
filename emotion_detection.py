import requests
import json


def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Get the dictionary for 'emotion'
    result = formatted_response['emotionPredictions'][0]['emotion']

    # Find the emotion with the maximum score
    dominant_emotion_key = max(result, key=result.get)

    # Add the dominant emotion to the result
    result['dominant_emotion'] = dominant_emotion_key

    # Return the response
    return result

