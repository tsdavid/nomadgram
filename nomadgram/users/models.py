from django.contrib.auth.models import AbstractUser
#from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not sepcified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    #미리 만들어진 user이후에 해당 필드들이 만들어지는 거기때문에 기본적으로 null을 해줘야
    #원래 만들어진 필드에도 적용된다.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140,null=True)
    gender = models.CharField(max_length=80 , choices=GENDER_CHOICE,null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


        


