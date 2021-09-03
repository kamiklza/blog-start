from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

# ------Official answer-------- #
# posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
# post_objects = []
# for post in posts:
#     post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
#     post_objects.append(post_obj)
# ---------Passing the post data into the object--------------#


@app.route('/')
def home():
    blog_posts = Post.get_post()
    return render_template("index.html", all_posts=blog_posts)


@app.route('/post/<int:index>')
def get_post(index):
    blog_posts = Post.get_post()
    for post in blog_posts:
        if post['id'] == index:
            display_post = post
    return render_template('post.html', post=display_post)


if __name__ == "__main__":
    app.run(debug=True)
