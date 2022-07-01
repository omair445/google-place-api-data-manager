from flask import jsonify


def success(msg='', data=None):
    if data is None:
        data = []
    return jsonify({
        'status': True,
        'message': msg,
        'status_code': 200,
        'total_count': len(data),
        'data': data
    })