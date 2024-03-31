
from django.contrib import auth
from django.db import models
from src.accounts.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, _user_has_perm
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import PermissionDenied

from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group

from src.core.modules import upload_image_file_path


def _user_has_model_op_perms(user, app_label, model_name):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_model_op_perms'):
            continue
        try:
            if backend.has_model_op_perms(user, app_label, model_name):
                return True
        except PermissionDenied:
            return False

    return False


class User(PermissionsMixin, AbstractBaseUser):
    # Custom user model supports email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)# Validators should be a list
    groups = models.ManyToManyField(Group,blank=True)
    about = models.TextField(_('about'),max_length=500,blank=True)
    dob = models.CharField(max_length=255,blank=True,null=True,help_text="Pattern = dd-mm-yyyy")

    facebook_url = models.URLField(max_length = 255, null=True, blank=True)
    twitter_url = models.URLField(max_length = 255, null=True, blank=True)
    linkedin_url = models.URLField(max_length = 255, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True,
                                default='uploads/user/default-user-avatar.png',
                                upload_to=upload_image_file_path)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email