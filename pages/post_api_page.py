import requests

class PostAPIPage:

    URL = "https://jsonplaceholder.typicode.com/posts"

    def get_a_post(self, post_id):
        response = requests.get(f"{self.URL}/{post_id}")
        return response

    def get_all_posts(self):
        response = requests.get(self.URL)
        return response
    
    def create_post(self, title, body, userId):
        data = {
            "title": title,
            "body": body,
            "userId": userId
        }
        response = requests.post(self.URL, json=data)
        return response