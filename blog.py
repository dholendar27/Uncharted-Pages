import base64
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from models import Post
from werkzeug.utils import secure_filename
from app import db
blog = Blueprint('blog',__name__,url_prefix='/blog', template_folder='templates/blog/', static_folder='static/')


@blog.route('/home',endpoint='home')
@login_required
def posts():
    posts = Post.query.filter(Post.user_id != current_user.id).all()
    posts_with_images = []

    for post in posts:
        if post.image:  # Ensure there is image data
            # Encode the binary data to Base64
            encoded_image = base64.b64encode(post.image).decode('utf-8')
            # Append the post data and encoded image to the list
            posts_with_images.append({
                'id': post.id,
                'title': post.title,
                'description': post.description,
                'image': encoded_image,
                'mimetype': post.mimetype,
                'markdown': post.markdown,
                'created_at': post.created_at,
                'user_id': post.user_id,
            })
    return render_template('home.html', user=current_user, cards=posts_with_images)

@blog.route('/posts',endpoint='posts')
@login_required
def posts():
    posts = Post.query.filter_by(user_id=current_user.id)
    posts_with_images = []

    for post in posts:
        if post.image:  # Ensure there is image data
            # Encode the binary data to Base64
            encoded_image = base64.b64encode(post.image).decode('utf-8')
            # Append the post data and encoded image to the list
            posts_with_images.append({
                'id': post.id,
                'title': post.title,
                'description': post.description,
                'image': encoded_image,
                'mimetype': post.mimetype,
                'markdown': post.markdown,
                'created_at': post.created_at,
                'user_id': post.user_id,
            })
    return render_template('posts.html', user=current_user, posts=posts_with_images)


@blog.route('/delete/<int:id>',endpoint='delete')
@login_required
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.posts'))



@blog.route('/create',endpoint='create', methods=["GET","POST"])
@login_required
def create_post():
    if request.method == "POST":
        image = request.files['image']
        title = request.form.get('title')
        description = request.form.get('description')
        markdown = request.form.get('markdown')
        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        img_data = image.read()
        new_post = Post(
                    title=title,
                    description=description,
                    markdown=markdown,
                    author=current_user,  # Use current_user to link to the User model
                    mimetype=mimetype,
                    image=img_data
                )

        # Save the Post object to the database
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.posts'))
    return render_template('blogpost.html', user=current_user,)