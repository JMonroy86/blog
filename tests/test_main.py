import unittest
import pytest
from blog.user.application import user


# class Test_Methods(unittest.TestCase):
#     def test_root(self):
#         final_result = root(1000)
#         self.assertEqual(1000, final_result)


class Test_users_application(unittest.TestCase):

    def test_create_an_user(self):
        expected = {"username": "string", "email": "user@example.com",
                    "is_active": True, "is_superuser": True}

        user_created = user.user_signup(
            {"username": "string", "email": "user@example.com", "password": "psw"})
        self.assertEqual(expected, user_created)

    def test_return_error_when_user_doesnt_exist(self):
        self.assertRaises(ValueError, user.user_signup, "two")

    # def test_find_existing_user_email(self):
    #     expected = {"username": "string", "email": "user@example.com",
    #                 "is_active": True, "is_superuser": True}


@pytest.mark.asyncio
async def test_create_an_user_db(mock_create_user):
    mocker_data = {"username": "string", "email": "user@example.com",
                   "is_active": True, "is_superuser": True}
    mock_create_user.return_value = mocker_data
    user_created = await user.user_signup({"username": "string", "email": "user@example.com"})
    assert user_created == mocker_data
