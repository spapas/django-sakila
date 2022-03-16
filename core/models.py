# This is an auto-generated Django model module.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    last_update = models.DateTimeField()

    def __str__(self):
        return self.last_name

    class Meta:
        managed = False
        db_table = "actor"


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    district = models.TextField()
    city = models.ForeignKey('City', models.PROTECT)
    postal_code = models.TextField(blank=True, null=True)
    phone = models.TextField()
    last_update = models.DateTimeField()

    def __str__(self):
        return self.address

    class Meta:
        managed = False
        db_table = "address"


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.TextField()
    last_update = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "category"


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.TextField()
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.city

    class Meta:
        managed = False
        db_table = "city"


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.TextField()
    last_update = models.DateTimeField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.country

    class Meta:
        managed = False
        db_table = "country"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store', on_delete=models.PROTECT)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    active = models.TextField()
    create_date = models.DateTimeField()  # This field type is a guess.
    last_update = models.DateTimeField()

    def __str__(self):
        return self.last_name

    class Meta:
        managed = False
        db_table = "customer"


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    release_year = models.TextField(blank=True, null=True)
    language = models.ForeignKey('Language', on_delete=models.PROTECT)
    original_language = models.ForeignKey('Language', on_delete=models.PROTECT, blank=True, null=True, related_name='+')
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    rating = models.TextField(blank=True, null=True)
    special_features = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = "film"


class FilmActor(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.PROTECT)
    film = models.ForeignKey('Film', on_delete=models.PROTECT)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.actor + '/' + self.film

    class Meta:
        managed = False
        db_table = "film_actor"


class FilmCategory(models.Model):
    film = models.ForeignKey('Film', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.category + '/' + self.film

    class Meta:
        managed = False
        db_table = "film_category"


class FilmText(models.Model):
    film_id = models.ForeignKey('Film', on_delete=models.PROTECT)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = "film_text"


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey('Film', on_delete=models.PROTECT)
    store = models.ForeignKey('Store', on_delete=models.PROTECT)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.inventory_id

    class Meta:
        managed = False
        db_table = "inventory"


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.TextField()
    last_update = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "language"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    staff = models.ForeignKey('Staff', on_delete=models.PROTECT)
    rental = models.ForeignKey('Rental', on_delete=models.PROTECT, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=5
    )  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    payment_date = models.TextField()  # This field type is a guess.
    last_update = models.DateTimeField()

    def __str__(self):
        return self.payment_id

    class Meta:
        managed = False
        db_table = "payment"


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()  # This field type is a guess.
    inventory = models.ForeignKey('Inventory', on_delete=models.PROTECT)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    return_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    staff = models.ForeignKey('Staff', on_delete=models.PROTECT)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.rental_date

    class Meta:
        managed = False
        db_table = "rental"
        unique_together = (("rental_date", "inventory_id", "customer_id"),)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    picture = models.BinaryField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    store = models.ForeignKey('Store', on_delete=models.PROTECT)
    active = models.SmallIntegerField()
    username = models.TextField()
    password = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.last_name

    class Meta:
        managed = False
        db_table = "staff"


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey('Staff', on_delete=models.PROTECT, related_name='+')
    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    last_update = models.DateTimeField()
    
    def __str__(self):
        return self.address

    class Meta:
        managed = False
        db_table = "store"
