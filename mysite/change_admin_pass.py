import argparse
import os

# has to be called prior to django lib import
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.contrib.auth.models import User


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('user', help="Django user name. If no such user exists"
                        " a superuser with given name will be created")
    parser.add_argument('password',
                        help="New password to set to the django user")
    args = parser.parse_args()
    user, created = User.objects.get_or_create(username=args.user)
    user.is_superuser = True
    user.is_staff = True
    user.set_password(args.password)
    user.save()


if __name__ == "__main__":
    main()
