from django.contrib import admin
from . import models


class ActorModelAdmin(admin.ModelAdmin):
    list_display = ("actor_id", "last_name", "first_name", "last_update")


class AddressModelAdmin(admin.ModelAdmin):
    list_display = (
        "address_id",
        "address",
        "address2",
        "district",
        "city",
        "postal_code",
        "phone",
    )


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("category_id", "name", "last_update")


class CityModelAdmin(admin.ModelAdmin):
    list_display = ("city_id", "city", "country", "last_update")


class CountryModelAdmin(admin.ModelAdmin):
    list_display = ("country_id", "country", "last_update")


class CustomerModelAdmin(admin.ModelAdmin):
    list_display = (
        "customer_id",
        "store",
        "first_name",
        "last_name",
        "email",
        "active",
        "last_update",
    )


class FilmActorModelAdmin(admin.ModelAdmin):
    list_display = ("actor", "film", "last_update")


class FilmCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("film", "category", "last_update")


class FilmModelAdmin(admin.ModelAdmin):
    list_display = (
        "film_id",
        "title",
        "description",
        "release_year",
        "language_id",
        "original_language_id",
        "rental_duration",
        "rental_rate",
        "length",
        "replacement_cost",
        "rating",
        "special_features",
        "last_update",
    )


class FilmTextModelAdmin(admin.ModelAdmin):
    list_display = (
        "film_id",
        "title",
        "description",
    )


class InventoryModelAdmin(admin.ModelAdmin):
    list_display = ("inventory_id", "film", "store", "last_update")


class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ("language_id", "name", "last_update")


class PaymentModelAdmin(admin.ModelAdmin):
    list_display = (
        "payment_id",
        "customer",
        "staff",
        "rental_id",
        "amount",
        "payment_date",
        "last_update",
    )


class RentalModelAdmin(admin.ModelAdmin):
    list_display = (
        "rental_id",
        "rental_date",
        "inventory",
        "customer",
        "return_date",
        "staff",
        "last_update",
    )


class StaffModelAdmin(admin.ModelAdmin):
    list_display = (
        "staff_id",
        "first_name",
        "last_name",
        "address_id",
        "picture",
        "email",
        "active",
        "store",
        "last_update",
    )


class StoreModelAdmin(admin.ModelAdmin):
    list_display = ("store_id", "manager_staff_id", "address_id", "last_update")


admin.site.register(models.Address, AddressModelAdmin)
admin.site.register(models.Actor, ActorModelAdmin)
admin.site.register(models.Category, CategoryModelAdmin)
admin.site.register(models.City, CityModelAdmin)
admin.site.register(models.Country, CountryModelAdmin)
admin.site.register(models.Customer, CustomerModelAdmin)
admin.site.register(models.FilmActor, FilmActorModelAdmin)
admin.site.register(models.FilmCategory, FilmCategoryModelAdmin)
admin.site.register(models.Film, FilmModelAdmin)
admin.site.register(models.FilmText, FilmTextModelAdmin)
admin.site.register(models.Inventory, InventoryModelAdmin)
admin.site.register(models.Language, LanguageModelAdmin)
admin.site.register(models.Payment, PaymentModelAdmin)
admin.site.register(models.Rental, RentalModelAdmin)
admin.site.register(models.Staff, StaffModelAdmin)
admin.site.register(models.Store, StoreModelAdmin)
