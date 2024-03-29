# from . import main

from flask import jsonify, request, url_for, current_app

from . import api
from ..models import ClassRoom


@api.route('/test/')
def test():
    return jsonify({"status": 1})


@api.route('/classrooms/')
def get_classrooms():
    page = request.args.get('page', 1, type=int)
    pagination = ClassRoom.query.paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    classrooms = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_classrooms', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_classrooms', page=page + 1)
    return jsonify({
        'classrooms': [classroom.to_json() for classroom in classrooms],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/classroom/')
def get_classroom():
    classroom_number = request.args.classroom_number
    post = ClassRoom.query.get_or_404(classroom_number)
    return jsonify(post.to_json())
