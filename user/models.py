from sorting.models import HouseResult, WandResult, FavouriteSection, FavouriteChoice

from django.db import models

class User(models.Model):
    email              = models.EmailField(max_length = 100, unique = True)
    password           = models.CharField(max_length = 200)
    first_name         = models.CharField(max_length = 100)
    last_name          = models.CharField(max_length = 100)
    date_of_birth      = models.DateField(auto_now = False)
    is_send_newsletter = models.BooleanField(null = True)
    google_id          = models.CharField(max_length = 100, null = True)
    created_at         = models.DateTimeField(auto_now_add = True)
    updated_at         = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'

class UserHouse(models.Model):
    user         = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    house_result = models.ForeignKey(HouseResult, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_houses'

class UserWand(models.Model):
    user        = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    wand_result = models.ForeignKey(WandResult, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_wands'

class UserFavourite(models.Model):
    user              = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    favourite_section = models.ForeignKey(FavouriteSection, on_delete = models.SET_NULL, null = True)
    favourite_choice  = models.ForeignKey(FavouriteChoice, on_delete = models.SET_NULL, null = True)

class Meta:
        db_table = 'user_favourites'
