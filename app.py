"""Flask app for sklearn boston housing price prediction."""
import logging
from flask import Flask, request, jsonify
from flask.logging import create_logger

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

APP = Flask(__name__)
LOG = create_logger(APP)
LOG.setLevel(logging.INFO)


def scale(payload):
    """Scales Payload to prepare it for prediction."""
    LOG.info("Scaling Payload: \n%s", payload)
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict


@APP.route("/")
def home():
    """Home route returning a simple HTML page."""
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)


@APP.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction.

    input looks like:
    {
    "CHAS":{"0":0},
    "RM":{"0":6.575},
    "TAX":{"0":296.0},
    "PTRATIO":{"0":15.3},
    "B":{"0":396.9},
    "LSTAT":{"0":4.98}
    }

    result looks like:
    { "prediction": [ <val> ] }
    """
    json_payload = request.json
    LOG.info("JSON payload: \n%s", json_payload)
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("Inference payload DataFrame: \n%s", inference_payload)
    scaled_payload = scale(inference_payload)
    prediction = list(CLF.predict(scaled_payload))
    LOG.info("Output prediction: \n%s", prediction)
    return jsonify({'prediction': prediction})


if __name__ == "__main__":
    CLF = joblib.load("./model_data/boston_housing_prediction.joblib")
    APP.run(host='0.0.0.0', port=80, debug=True)
