from tests import TestUser, TestUserService, TestUserUtil

if __name__ == "__main__":
    print(TestUser().test_user_creation())
    print(TestUserService().test_user_service())
    print(TestUserUtil().test_user_util())
