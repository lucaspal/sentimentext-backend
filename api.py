#!/usr/bin/env python3.7
import json
import flask
from sentiment import sentiment, scrape

app = flask.Flask(__name__)

@app.route('/sentimentext/api/analyze')
def analyze():
    url = flask.request.args.get('url')
    title, text, err = scrape(url)
    title_sent = sentiment(title)
    text_sent = sentiment(text)
    res = {'title': title,
        'sentiment': { 
            'title': {'polarity': title_sent.polarity,
                        'subjectivity': title_sent.subjectivity},
            'text': {'polarity': text_sent.polarity,
                        'subjectivity': text_sent.subjectivity}}}
    return flask.jsonify(res)

@app.errorhandler(404)
def page_not_found(e):
    return flask.jsonify(error=404, text=str(e)), 404

@app.errorhandler(500)
def internal_error(e):
    return flask.jsonify(error=500, text=str(e)), 500

if __name__=='__main__':
    app.run(debug=False, port=80)
