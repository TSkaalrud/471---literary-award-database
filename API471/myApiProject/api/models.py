from django.db import models
from datetime import date
from django import forms
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

#from django_mysql.models import ListCharField
#from django.contrib.auth.models import User

#Base user class
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    isAuthor = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.username



# Create your models here.
##class User(AbstractUser):
##
##    class Types(models.TextChoices):
##        AUTHOR = "AUTHOR", "Author"
##        ADMIN = "ADMIN", "Admin"
##
##    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.AUTHOR)
##
##    name = models.CharField(_("Name of User"), blank=True, max_length=255)
##
##    def get_absolute_url(self):
##        return reverse("users:detail", kwargs={"username": self.username})
##
##class AuthorManager(models.Manager):
##    def get_queryset(self, *args, **kwargs):
##        return super().get_queryset(*args, **kwargs).filter(type=User.Types.AUTHOR)
##
##class AdminManager(models.Manager):
##    def get_queryset(self, *args, **kwargs):
##        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)
##
##class Author(User):
##    class Meta:
##        proxy = True
##
##class Admin(User):
##    class Meta:
##        proxy = True
    
#new addition to hold the list of Author PublishedWorks
class PubWork(models.Model):
    WorkName = models.CharField(max_length=100)

#authors
class Author(models.Model):
    Emerging_Established = (
        ('M', 'Emerging'),
        ('S', 'Established'),
    )
    AuthorName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100)
    SexualOrientation = models.CharField(max_length=100)
    Race = models.CharField(max_length=100)
    Residency = models.CharField(max_length=100)
    EstablishedVSEmerging = models.CharField(max_length=1, choices=Emerging_Established)
    PublishedWorks = models.ManyToManyField(PubWork)
    Citizenship = models.CharField(max_length=100)

#publishers
class Publisher(models.Model):
    PublisherName = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)

#Published Work items
#Added Name field because published works have names
class Work(models.Model):
    AuthorName = models.ForeignKey(Author, on_delete=models.CASCADE)
    PublisherName = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    WorkName = models.CharField(max_length=100)
    PageCount = models.IntegerField()
    Genre = models.CharField(max_length=100)
    Form = models.CharField(max_length=100)
    Setting = models.CharField(max_length=100)
    SubjectMatter = models.CharField(max_length=100)
    PublishingRoute = models.CharField(max_length=100)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['AuthorName', 'PublisherName', 'WorkName'], name='Work_key')
        ]

#class Nominator(models.Model): unnecessary?

#Third Parties
class ThirdParty(models.Model):
    PartyName = models.CharField(max_length=100, primary_key=True)

#publications
class Publication(models.Model):
    PublisherName = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    AuthorName = models.ForeignKey(Author, on_delete=models.CASCADE)
    PublishingFormat = models.CharField(max_length=100)
    PrintRunSize = models.IntegerField()
    PublicationDate = forms.DateField(
        widget=forms.DateInput(format=('%d-%m-%Y')))
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['PublisherName', 'AuthorName'], name='Pub_key')
        ]
        


#class Nominatable(models.Model): unnecessary?

#Donors of literary awards
class Donor(models.Model):
    Public = (
        ('T', 'True'),
        ('F', 'False'),
    )
    Name = models.CharField(max_length=100, primary_key=True)
    PublicName = models.CharField(max_length=1, choices=Public)

#Literary Awards
#uses ThirdParty pk for Nominator
class LiteraryAward(models.Model):
    NominatorName = models.ForeignKey(ThirdParty, on_delete=models.CASCADE)
    DonorName = models.ForeignKey(Donor, on_delete=models.CASCADE)
    AuthorAwardCNumber = models.IntegerField()
    AwardCNumber = models.IntegerField()
    WorkAwardCNumber = models.IntegerField()
    Organization = models.CharField(max_length=100)
    AwardFrequency = models.CharField(max_length=100)
    MonetaryValue = models.IntegerField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['NominatorName', 'DonorName'], name='Lit_key')
        ]



#class Criteria(models.Model): unnecessary?

#Mutual Exclusivity lists for Award based criteria
#new addition to hold a MutuallyExclusiveList
class MEList(models.Model):
    #List = ListCharField(
    #    base_field=CharField(max_length=50),
    #    size=10
    #)
    List = models.JSONField()

#Award based criteria for Literary awards
class AwardBased(models.Model):
    MutuallyExclusiveList = models.ForeignKey(MEList, on_delete=models.CASCADE)


#Criteria for literary awards based on the Work involved 
class WorkBased(models.Model):
    Form = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    Setting = models.CharField(max_length=100)
    NoOfWorks = models.IntegerField()
    SubjectMatter = models.CharField(max_length=100)
    PageCount = models.IntegerField()
    RequiredSales = models.IntegerField()
    PublicationDate = forms.DateField(
        widget=forms.DateInput(format=('%d-%m-%Y')))
    PublicationLocation = models.CharField(max_length=100)
    PrintRunSize = models.IntegerField()
    PublishingRoute = models.CharField(max_length=100)
    PublishingFormat = models.CharField(max_length=100)

#Criteria for literary awards based on the Author involved
class AuthorBased(models.Model):
    Emerging_Established = (
        ('M', 'Emerging'),
        ('S', 'Established'),
    )

    Race = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    SexualOrientation = models.CharField(max_length=100)
    Residency = models.CharField(max_length=100)
    Citizenship = models.CharField(max_length=100)
    EstablishedVSEmerging = models.CharField(max_length=1, choices=Emerging_Established)
    Age = models.IntegerField()    

#Vendors of author/work sales
class Vendor(models.Model):
    Name = models.CharField(max_length=100, primary_key=True)

#sales of author's works by a vendor 
class Sell(models.Model):
    W_Name = models.ForeignKey(Author, on_delete=models.CASCADE)
    V_Name = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Sales = models.DecimalField(decimal_places=2, max_digits=50)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['W_Name', 'V_Name'], name='Sell_key')
        ]
