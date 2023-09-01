from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://app.ylytic.com/ylytic/test"

def fetch_comments():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    return []

@app.route('/search', methods=['GET'])
def search_comments():
    comments = fetch_comments()
    filtered_comments = []

    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = int(request.args.get('like_from', 0))
    like_to = int(request.args.get('like_to', float('inf')))
    reply_from = int(request.args.get('reply_from', 0))
    reply_to = int(request.args.get('reply_to', float('inf')))
    search_text = request.args.get('search_text')

    for comment in comments:
        if (search_author is None or search_author in comment['author']) and \
           (at_from is None or comment['at'] >= at_from) and \
           (at_to is None or comment['at'] <= at_to) and \
           (like_from <= comment['like'] <= like_to) and \
           (reply_from <= comment['reply'] <= reply_to) and \
           (search_text is None or search_text in comment['text']):
            filtered_comments.append(comment)

    return jsonify(filtered_comments)

if __name__ == '__main__':
    app.run()
