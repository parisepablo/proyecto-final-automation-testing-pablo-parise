import requests

class PostAPIPage:

    URL = "https://jsonplaceholder.typicode.com/posts"

    def get_posts(self, post_id):
        response = requests.get(f"{self.URL}/{post_id}")
        return response