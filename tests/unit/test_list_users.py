from lib.list_users import handler
from hamcrest import assert_that, equal_to


def test_list_users(context):
    event = {}

    response = handler(event, context)

    assert_that(response["statusCode"], equal_to(200))
