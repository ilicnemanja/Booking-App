from django.db import models
import bcrypt


class Person(models.Model):

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=254, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=150, null=False)
    is_owner = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.is_owner:
            return f"{self.first_name} {self.last_name} (owner)"
        return f"{self.first_name} {self.last_name}"

    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        return hashed_password

    def verify_password(self, password, hashed_password):
        check_password = bcrypt.checkpw(password.encode('utf8'), hashed_password)
        if check_password:
            return True
        return False