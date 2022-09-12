from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email or not username:
            raise ValueError("Email, username are required fields")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        ) 
        user.set_password(password)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username        = models.CharField(max_length=30, unique=True)
    email           = models.EmailField(max_length=60, unique=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    profile_image   = models.ImageField(max_length=255, 
                                      upload_to='media/profile_images', 
                                      default='media/default_profile_image', 
                                      null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Tag(models.Model):
    title           = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.title

class Post(models.Model):
    title           = models.CharField(max_length=30)
    content         = models.TextField()
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags            = models.ManyToManyField(Tag)
    picture         = models.ImageField(max_length=255, 
                                        upload_to='media/post_images', 
                                        default='media/default_post_image', 
                                        null=True, blank=True)

    def __str__(self):
        return self.title

