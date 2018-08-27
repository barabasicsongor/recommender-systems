from flask import Flask, request, jsonify
from top_items import get_top_items
from collab_recomm import get_collab_recommendation
import json

"""
FLASK APP
"""

app = Flask(__name__)


@app.route('/')
def base():
    return "Hi"

@app.route('/top-items', methods=['POST'])
def top_items_recommendation():
    data = request.get_json(force=True)
    items = data["items"]
    top_items = get_top_items(items)

    return top_items

@app.route('/collab-filt', methods=['POST'])
def collab_filt_recommendation():
    data = request.get_json(force=True)
    ratings = data['ratings']
    pred_user = data['recomm_user_id']

    recommendation = get_collab_recommendation(ratings, pred_user)

    result = {'result': recommendation}

    return json.dumps(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
