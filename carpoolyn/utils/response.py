from flask import jsonify


def success(msg='', data=None):
    if data is None:
        data = []
    return jsonify({
        'status': 200,
        'message': msg,
        'total_count': len(data),
        'data': data
    })