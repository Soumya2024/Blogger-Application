from flask import Blueprint, request, jsonify
from models import Post, Comment
from auth import token_required
from extensions import db

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    op = []
    for po in posts:
        ps = po.to_dict()
        op.append(ps)
    # return render_template('create_post.html')
    return jsonify(op), 200

@blog_bp.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    ps_dt = post.to_dict()
    cs = []
    for ct in post.comments:
        cs.append(ct.to_dict())
    ps_dt['comments'] = cs
    
    # return render_template('single_post.html', post=post)
    return jsonify(ps_dt), 200

@blog_bp.route('/api/posts', methods=['POST'])
@token_required
def create_post(current_user):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'data missing'}), 400
    new_post = Post(
        title=data['title'],
        content=data['content'],
        user_id=current_user.id
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'created', 'post': new_post.to_dict()}), 201

@blog_bp.route('/api/posts/<int:post_id>', methods=['PUT'])
@token_required
def update_post(current_user, post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        return jsonify({'message': 'cannot edit'}), 400
    
    data = request.get_json()
    if data.get('title'):
        post.title = data['title']
    if data.get('content'):
        post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'updated', 'post': post.to_dict()}), 201

@blog_bp.route('/api/posts/<int:post_id>', methods=['DELETE'])
@token_required
def delete_post(current_user, post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        return jsonify({'message': 'delete not possible'}), 403
    db.session.delete(post)
    db.session.commit()
    
    return jsonify({'message': 'deleted'}), 204