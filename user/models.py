from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)




class User(AbstractUser):

    username = None
    first_name = None
    last_name = None

    inn = models.CharField('ИНН', max_length=255, blank=True, null=True)
    email = models.EmailField('Эл. почта',blank=True,null=True, unique=True)
    fio = models.CharField('ФИО', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True,unique=True)
    profile_ok = models.BooleanField(default=False)
    total_summ = models.IntegerField(default=0)
    need_to_next_level = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'Аккаунт. ID {self.id}, Дата регистрации: {self.date_joined}'

    def save(self, *args, **kwargs):
        print(self.total_summ)
        if self.total_summ >= 50000:
            self.discount = 1
            self.need_to_next_level = 100000 - self.total_summ
        elif self.total_summ >= 100000:
            self.discount = 2
            self.need_to_next_level = 150000 - self.total_summ
        elif self.total_summ >= 150000:
            self.discount = 3
            self.need_to_next_level = 200000 - self.total_summ
        elif self.total_summ >= 200000:
            self.discount = 4
            self.need_to_next_level = 250000 - self.total_summ
        elif self.total_summ >= 250000:
            self.discount = 5
        else:
            self.need_to_next_level = 50000 - self.total_summ
        super(User, self).save(*args, **kwargs)




class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='addresses')
    street = models.CharField( max_length=50, blank=True, null=True)
    house = models.CharField( max_length=50, blank=True, null=True)
    flat = models.CharField( max_length=50, blank=True, null=True)
    podezd = models.CharField( max_length=50, blank=True, null=True)
    code = models.CharField( max_length=50, blank=True, null=True)
    floor = models.CharField( max_length=50, blank=True, null=True)


