import pytest

from pages.post_api_page import PostAPIPage
from utils.logger import logger
import pytest_check as check

api = PostAPIPage()
logger = logger()

def test_get_a_post():
    logger.info("Starting get a post test")
    post_id = 1
    response = api.get_a_post(post_id)
    logger.info(f"Response for post {post_id}: {response.json()}")
    #validates the response status code and the post id
    check.equal(response.status_code, 200, f"Expected code 200 but got {response.status_code}")
    body = response.json()
    check.equal(body["id"], post_id, f"Expected id {post_id} but got {body['id']}")

def test_get_all_posts():
    logger.info("Starting get all posts test")
    response = api.get_all_posts()
    logger.info(f"Response for all posts: {response.json()}")
    #validates the response status code, the number of posts, and the response type
    check.equal(response.status_code, 200, f"Expected code 200 but got {response.status_code}")
    posts = response.json()
    check.greater(len(posts), 0, "Expected at least one post but got none")
    check.is_true(
        isinstance(posts, list), "Expected response to be a list of posts"
    )

def test_create_post(post_data):
    logger.info("Starting create post test")
    response = api.create_post(
        post_data["title"],
        post_data["body"],
        post_data["userId"]
        )
    logger.info(f"Response for creating post: {response.json()}")
    #validates the response status code and the response type
    check.equal(response.status_code, 201, f"Expected code 201 but got {response.status_code}")
    created_post = response.json()
    check.is_true(
        isinstance(created_post, dict), "Expected response to be a dictionary"
    )