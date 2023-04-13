from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from request_driver import options
from two_ml_models import CoverTypeClassifier

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return {"Flask Status": "loaded"}


@app.route('/predict', methods=['POST'])
def predict():
    picked_option = request.json['option']
    sample_pred = np.array(request.json['pred_input'])
    print("picked_option = ", picked_option)
    print("sample_pred = ", sample_pred)

    output_json = {}
    output_json.clear()
    if picked_option == options[0]:
        print(picked_option)
    elif picked_option == options[1]:
        classifier = CoverTypeClassifier(data_file_path='covtype.data')
        random_forest_acc = classifier.get_random_forest_accuracy()
        logistic_reg_acc = classifier.get_logistic_regression_accuracy()
        predicted_cover_type = classifier.predict_cover_type(sample_pred)
        predicted_cover_type = np.int64(predicted_cover_type).tolist()
        output_json = {"Random Forest Accuracy": random_forest_acc, "Logistic Regression Accuracy:": logistic_reg_acc,
                       "Predict 'Cover_type' value for sample": predicted_cover_type}
    elif picked_option == options[2]:
        print(picked_option)
    else:
        return jsonify({'error': 'Invalid option choice.'}), 400

    return jsonify(output_json)


if __name__ == '__main__':
    app.run(port=8080)