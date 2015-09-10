__author__ = 'Lovebonito'
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images',blank=True)

    def __unicode__(self):
        return self.user.username


class Regions(models.Model):
    regionid = models.IntegerField(db_column='RegionID', primary_key=True)  # Field name made lowercase.
    regiondescription = models.TextField(db_column='RegionDescription')  # Field name made lowercase.

    class Meta:
        db_table = 'Regions'


class Shippers(models.Model):
    shipperid = models.IntegerField(db_column='ShipperID', primary_key=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Shippers'


class Suppliers(models.Model):
    supplierid = models.IntegerField(db_column='SupplierID', primary_key=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName')  # Field name made lowercase.
    contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
    contacttitle = models.TextField(db_column='ContactTitle', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
    homepage = models.TextField(db_column='HomePage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Suppliers'


class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title