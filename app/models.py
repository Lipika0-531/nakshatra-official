from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.utils import timezone


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()


class Categories(models.Model):
    title = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=18)
    description = models.CharField(max_length=200)
    image_URl = models.ImageField(upload_to="images/")
    publised_on = models.DateTimeField(editable=False)
    price = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0, null=True)
    avg_ratings = models.IntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    rating_count = models.PositiveIntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.publised_on = timezone.now()
        return super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    body = models.TextField(max_length=4000, null=True)
    created_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Reviews, self).save(*args, **kwargs)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
