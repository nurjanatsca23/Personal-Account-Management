from datetime import date
from user import User
from user_service import UserService
from user_util import UserUtil


class TestUser:

    def test_user_creation(self):
        user = User(
            "240000001",
            "Nurjanat",
            "Sultanova",
            "nurjanat.sultanova@gmail.com",
            "Password1!",
            date(2008, 1, 29)
        )

        assert user.name == "Nurjanat"
        return "TestUser passed successfully"


class TestUserService:

    def test_user_service(self):
        service = UserService()

        user1 = User(
            "240000001",
            "Nurjanat",
            "Sultanova",
            "nurjanat.sultanova@gmail.com",
            "Password1!",
            date(2008, 1, 29)
        )

        service.add_user(user1)
        assert service.find_user("240000001") == user1
        return "TestUserService passed successfully"


class TestUserUtil:

    def test_user_util(self):
        util = UserUtil()
        user_id = util.generate_user_id()
        assert len(user_id) == 9
        return "TestUserUtil passed successfully"
