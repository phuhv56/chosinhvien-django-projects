from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
from django.utils.timesince import timesince
from django import template
# Create your models here.



class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey('Category')
    area = models.ForeignKey('Area')
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/upload/%y/%m', blank=True)
    quantity = models.IntegerField()
    time_post = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=0)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        s = self.name
        u = unicode(s)
        self.slug = slugify('%s %s %s' % (s, self.id, self.time_post, ))
        super(Product, self).save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Anonymous(models.Model):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    product = models.ForeignKey('Product')

    def __unicode__(self):
        return self.phone

 # create new user model
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    sex = models.BooleanField(default=0)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    facebook = models.CharField(max_length=100)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
