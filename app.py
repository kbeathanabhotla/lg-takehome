from flask import Flask, jsonify, request

app = Flask(__name__)

from project.pred_service import get_prediction


@app.route('/', methods=['POST'])
def predict_image_class():
    req = request.json
    pred = get_prediction(req.get('image_bytes'))
    return jsonify(pred)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
