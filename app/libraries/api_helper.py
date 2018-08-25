from flask import Response, jsonify, request
import json

MESSAGE_ERROR = {
    200: 'OK',
    400: 'Bad Request.',
    403: 'Forbidden.',
    404: 'Page not found.',
    405: 'Method not allowed.',
    410: 'Unauthorized.',
    500: 'Internal Server Error.',
    1001: 'Error DB Connection.',
    1002: 'Invalid Query.',
    1003: 'Data not found.',
    1004: 'Token Mismatch.',
    1005: 'Not Authorized.',
    1006: 'Invalid Parameter.',
    1007: 'Failed CRUD to Database.',
    1008: 'Bad Syntax.'
}

def response(status, data=''):
    """
    Function to get response API
    """

    result = {'code': status}
    result['status'] = MESSAGE_ERROR[status]
    result['message'] = data

    result = dict_to_json(result)
    res = Response(result, status=200, mimetype='application/json')
    res.headers['X-Robots-Tag'] = 'noindex, nofollow, noarchive, noodp, noydir, noarchive, nosnippet'
    res.headers['Connection'] = "close"
    return res


def my_converter(value):
    """
    my_converter : Convert datetime
    """

    if isinstance(value, datetime.datetime):
        return value.__str__()

def dict_to_json(detail_log):
    """ my_converter """
    return json.dumps(detail_log, sort_keys=True, default=my_converter)