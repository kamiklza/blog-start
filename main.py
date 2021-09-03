from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = Post.get_post()
    return render_template("index.html", all_posts=blog_posts)

@app.route('/<num>')
def get_post(num):
    blog_posts = Post.get_post()
    for post in blog_posts:
        if str(post['id']) == num:
            display_post = post
    return render_template('post.html', post=display_post)


if __name__ == "__main__":
    app.run(debug=True)
