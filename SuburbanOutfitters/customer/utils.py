from django.contrib.auth.models import User

def create_user(username, password, email=None):
    """
    Create a new user with the provided username, password, and email.
    """
    user = User.objects.create_user(username, email=email, password=password)
    return user