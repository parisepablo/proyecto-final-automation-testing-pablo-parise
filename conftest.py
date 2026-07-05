import pytest

@pytest.fixture
def post_data():
    return [
        "title": "First post title",
        "body": "First post body",
        "userId": 1
    ]

@pytest.fixture
def user_data():
    return [
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company"
    ]