from datetime import date
import random
import string

class UserUtil:

    @staticmethod
    def generate_user_id():
        year_prefix = str(date.today().year)[-2:]
        random_digits = ''.join(random.choices(string.digits, k=7))
        return year_prefix + random_digits

    @staticmethod
    def generate_password():
        upper = random.choice(string.ascii_uppercase)
        lower = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special = random.choice("!@#$%^&*()")

        remaining = ''.join(random.choices(
            string.ascii_letters + string.digits + "!@#$%^&*()", k=4
        ))

        password_list = list(upper + lower + digit + special + remaining)
        random.shuffle(password_list)

        return ''.join(password_list)

    @staticmethod
    def is_strong_password(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*()" for c in password)
        )

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        if "@" not in email:
            return False
        local, domain = email.split("@")
        if "." not in domain:
            return False
        if "." not in local:
            return False
        return True
