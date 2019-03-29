#!/usr/bin/python
"""
This example is based on
    * https://bottlepy.org/docs/dev
"""
import json

import bottle
from bottle import request, response
from bottle import error

app = application = bottle.Bottle()


@app.error(404)
def error404(error):
    return 'he is dead jim'


@app.route('/static/<filename:path>')
def static(filename):
    '''
    Serve static files
    '''
    return bottle.static_file(filename, root='./static')


@app.route('/')
@app.route('/<name>')
def main(name="Jim"):
    '''
    The front "index" page
    '''
    return bottle.template('Hello {{name}}', name=name)


@app.post('/api')
def post_api_request():
    try:
        # parse input data
        data = request.json

        if data is None:
            raise ValueError
    except ValueError:
        # if bad request data, return 400 Bad Request
        bottle.response.status = 400
        return

    # return 200 Success
    bottle.response.headers['Content-Type'] = 'application/json'
    return json.dumps({'request': data})


class StripPathMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.app(e, h)


if __name__ == '__main__':
    bottle.run(
        app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=8081,
        debug=True,
        reloader=True
    )
