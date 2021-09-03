import requests

class Post:
    def get_post():
        post_url = "https://api.npoint.io/7bb7d1b262b40d632b71"
        response = requests.get(url=post_url)
        all_posts = response.json()
        return all_posts
