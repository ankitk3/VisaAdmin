# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BookingPassengers(models.Model):
    visa_booking = models.ForeignKey('VisaBooking', models.DO_NOTHING)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    middle_name = models.CharField(max_length=45, blank=True, null=True)
    date_of_birth = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    occupation = models.CharField(max_length=45, blank=True, null=True)
    religion = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return 'Pax: ' + self.first_name
    class Meta:
        managed = False
        db_table = 'booking_passengers'


class BookingPricing(models.Model):
    id = models.IntegerField(primary_key=True)
    visa_booking = models.ForeignKey('VisaBooking', models.DO_NOTHING)
    cost = models.CharField(max_length=45, blank=True, null=True)
    service_charge = models.CharField(max_length=45, blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    roe = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return 'Pricing: ' + self.id
    class Meta:
        managed = False
        db_table = 'booking_pricing'


class BookingVisaDetails(models.Model):
    visa_booking = models.ForeignKey('VisaBooking', models.DO_NOTHING)
    visa_status = models.CharField(max_length=45, blank=True, null=True)
    country_code = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_visa_details'


class Cities(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    countries = models.ForeignKey('Countries', models.DO_NOTHING)
    flights_code = models.CharField(max_length=45, blank=True, null=True)
    hotels_code = models.CharField(max_length=45, blank=True, null=True)
    holidays_code = models.CharField(max_length=45, blank=True, null=True)
    code = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'cities'


class Countries(models.Model):
    name = models.CharField(max_length=45)
    active = models.IntegerField()
    code = models.CharField(max_length=45)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'countries'


class CountriesHasVendors(models.Model):
    countries = models.ForeignKey(Countries, models.DO_NOTHING, primary_key=True)
    vendors = models.ForeignKey('Vendors', models.DO_NOTHING)
    disabled = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.countries
    class Meta:
        managed = False
        db_table = 'countries_has_vendors'
        unique_together = (('countries', 'vendors'),)

class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.type
    class Meta:
        managed = False
        db_table = 'documents'


class TypeOfVisas(models.Model):
    visas = models.ForeignKey('Visas', models.DO_NOTHING)
    name = models.CharField(max_length=45, blank=True, null=True)
    min_processing_time = models.CharField(max_length=45, blank=True, null=True)
    max_processing_time = models.CharField(max_length=45, blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    roe = models.CharField(max_length=45, blank=True, null=True)
    vendor = models.ForeignKey('Vendors', models.DO_NOTHING)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'type_of_visas'


class TypeOfVisasDocuments(models.Model):
    type_of_visas = models.ForeignKey(TypeOfVisas, models.DO_NOTHING, primary_key=True)
    documents = models.ForeignKey(Documents, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'type_of_visas_documents'
        unique_together = (('type_of_visas', 'documents'),)


class VendorRoe(models.Model):
    vendor = models.ForeignKey('Vendors', models.DO_NOTHING)
    from_field = models.DateTimeField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField(blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    roe = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_roe'


class Vendors(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'vendors'


class VisaBooking(models.Model):
    booking_id = models.CharField(unique=True, max_length=45)
    ref_booking_id = models.CharField(max_length=45, blank=True, null=True)
    mode = models.CharField(max_length=45, blank=True, null=True)
    email_id = models.CharField(max_length=45, blank=True, null=True)
    mobile_number = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visa_booking'


class VisaPrice(models.Model):
    type_of_visas = models.ForeignKey(TypeOfVisas, models.DO_NOTHING)
    from_age = models.CharField(max_length=45, blank=True, null=True)
    to_age = models.CharField(max_length=45, blank=True, null=True)
    cost = models.CharField(max_length=45, blank=True, null=True)
    service_charge = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.type_of_visas
    class Meta:
        managed = False
        db_table = 'visa_price'


class Visas(models.Model):
    countries = models.ForeignKey(Countries, models.DO_NOTHING)
    name = models.CharField(max_length=45, blank=True, null=True)
    tnc = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    validity = models.CharField(max_length=45, blank=True, null=True)
    duration = models.CharField(max_length=45, blank=True, null=True)
    multientry = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'visas'
