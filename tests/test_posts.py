import pytest

from pages.post_api_page import PostAPIPage
from utils.logger import get_logger

api = PostAPIPage()
logger = get_logger()

def test_get_posts():
    logger.info("Starting test_get_posts")
    post_id = 1
    response = api.get_posts(post_id)
    logger.info(f"Response for post {post_id}: {response.json()}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id