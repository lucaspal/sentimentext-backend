from app import app
from app.helper import response
from app.sentiment import sentiment, scrape
from urllib.parse import urlparse
import flask

@app.route('/sentimentext/api/analyze')
def analyze():
    raw_url = flask.request.args.get('url')
    url = urlparse(raw_url).geturl()
    
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
def route_not_found(e):
    """
    Return a custom 404 Http response message for missing or not found routes.
    :param e: Exception
    :return: Http Response
    """
    return response('failed', 'Endpoint not found', 404)


@app.errorhandler(405)
def method_not_found(e):
    """
    Custom response for methods not allowed for the requested URLs
    :param e: Exception
    :return:
    """
    return response('failed', 'The method is not allowed for the requested URL', 405)


@app.errorhandler(500)
def internal_server_error(e):
    """
    Return a custom message for a 500 internal error
    :param e: Exception
    :return:
    """
    return response('failed', 'Internal server error', 500)
