from __future__ import unicode_literals

from django.db import models


class Customerdemographics(models.Model):
    customertypeid = models.TextField(db_column='CustomerTypeID', primary_key=True)  # Field name made lowercase.
    customerdesc = models.TextField(db_column='CustomerDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerDemographics'


class Customers(models.Model):
    customerid = models.TextField(db_column='CustomerID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
    contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
    contacttitle = models.TextField(db_column='ContactTitle', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Regions(models.Model):
    regionid = models.IntegerField(db_column='RegionID', primary_key=True)  # Field name made lowercase.
    regiondescription = models.TextField(db_column='RegionDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Regions'


class Shippers(models.Model):
    shipperid = models.IntegerField(db_column='ShipperID', primary_key=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'Suppliers'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RangoCategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'rango_category'


class RangoPage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=200)
    views = models.IntegerField()
    category = models.ForeignKey(RangoCategory)

    class Meta:
        managed = False
        db_table = 'rango_page'