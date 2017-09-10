from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser)


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Users must have a valid username.')

        account = self.model(
            username=username
        )

        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)

        account.is_admin = True
        account.save()
        return account