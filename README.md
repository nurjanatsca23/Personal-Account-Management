

## User Class

Represents a user in the system.

### Attributes:
`user_id` (int) – Unique identifier  
`name` (str) – First name  
`surname` (str) – Last name  
`email` (str) – Email address  
`password` (str) – User password  
`birthday` (date) – Date of birth  

### Methods:
- `get_details()` – Returns formatted user information  
- `get_age()` – Calculates and returns user age  


## UserService Class

Manages users using a class-level dictionary.

### Class Attribute:
- `users` – Dictionary storing all users  
  - key → `user_id`  
  - value → `User` object  

### Class Methods:
- `add_user(cls, user)`
- `find_user(cls, user_id)`
- `delete_user(cls, user_id)`
- `update_user(cls, user_id, user_update)`
- `get_number(cls)`


##  UserUtil Class

Provides helper utility functions.

### Static Methods:
- `generate_user_id()`
- `generate_password()`
- `is_strong_password(password)`
- `generate_email(name, surname, domain)`
- `validate_email(email)`


# Unit Testing

The project includes three test classes:

- `TestUser`
- `TestUserService`
- `TestUserUtil`

All tests are executed inside `main.py`.

# Sample Output

TestUser passed successfully
TestUserService passed successfully
TestUserUtil passed successfully



# UML Class Diagram

```
+-----------------------------+
|            User             |
+-----------------------------+
| - user_id : int             |
| - name : str                |
| - surname : str             |
| - email : str               |
| - password : str            |
| - birthday : date           |
+-----------------------------+
| + get_details() : str       |
| + get_age() : int           |
+-----------------------------+


+--------------------------------------------+
|               UserService                  |
+--------------------------------------------+
| - users : dict                             |
+--------------------------------------------+
| + add_user(user) <<class method>>          |
| + find_user(user_id) <<class method>>      |
| + delete_user(user_id) <<class method>>    |
| + update_user(user_id,user_update) <<class method>> |
| + get_number() <<class method>>            |
+--------------------------------------------+


+------------------------------------------------+
|                  UserUtil                      |
+------------------------------------------------+
| (no attributes)                                |
+------------------------------------------------+
| + generate_user_id() <<static>>                |
| + generate_password() <<static>>               |
| + is_strong_password(password) <<static>>      |
| + generate_email(name,surname,domain) <<static>>|
| + validate_email(email) <<static>>             |
+------------------------------------------------+
```

# Relationships

- `UserService` aggregates `User` objects (stores them in dictionary).
- `UserUtil` provides independent utility methods.
- `User` represents a single user entity.


