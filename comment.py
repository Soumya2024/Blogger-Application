from flask import Blueprint, request, jsonify
from extensions import db
from models import Post, Comment, db

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/api/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    post = Post.query.get_or_404(post_id)
    cd = []
    for comment in post.comments:
        cd.append(comment.to_dict())
    
    return jsonify(cd)

@comment_bp.route('/api/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data is not present'}), 400
    nc = Comment(
        name=data['name'],
        content=data['content'],
        post_id=post_id
    )
    db.session.add(nc)
    db.session.commit()
    return jsonify({'message': 'added', 'comment': nc.to_dict()}), 201
