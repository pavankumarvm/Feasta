from django.contrib.auth.base_user import BaseUserManager

class FeastaUserManager(BaseUserManager):

    def create_user(self, username, email, phone_no, first_name, last_name, is_messowner, is_consumer, password=None):
        """
            Creates and saves a User with given username,email and password
        """

        if not username:
            raise ValueError("Users must provide username")
        if not email:
            raise ValueError("Users must provide Emails")

        user = self.model(username=username, email = self.normalize_email(email))
        user.phone_no = phone_no
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_messowner = is_messowner
        user.is_consumer = is_consumer

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(username=username, email = self.normalize_email(email))
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using = self._db)
        return user
