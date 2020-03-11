from django.db import models

class User(models.Model):
    email            = models.CharField(max_length = 100)
    password         = models.CharField(max_length = 200)
    first_name       = models.CharField(max_length = 100)
    last_name        = models.CharField(max_length = 100, null = True)
    date_of_birth    = models.DateField(null = True)
    send_mail_is     = models.BooleanField(null = True)
    google_id        = models.CharField(max_length = 100, null = True)
    house            = models.ForeignKey('HouseResult', on_delete = models.SET_NULL, null = True)
    wand             = models.ForeignKey('WandResult', on_delete = models.SET_NULL, null = True)
    characters       = models.ForeignKey('FavouriteChoice', on_delete = models.SET_NULL, null = True)
    spells_potions   = models.ForeignKey('FavouriteChoice', on_delete = models.SET_NULL, null = True)
    places_transport = models.ForeignKey('FavouriteChoice', on_delete = models.SET_NULL, null = True)
    beasts_beings    = models.ForeignKey('FavouriteChoice', on_delete = models.SET_NULL, null = True)
    quidditch_teams  = models.ForeignKey('FavouriteChoice', on_delete = models.SET_NULL, null = True)
    objects_food     = models.ForeignKey('FavouriteChoice', on_delete = models.SET_NULL, null = True)
    created_at       = models.DateTimeField(auto_now_add = True)
    updated_at       = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'
