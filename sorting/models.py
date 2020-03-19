from django.db import models


class Passport(models.Model):
    section     = models.CharField(max_length = 50)
    title       = models.CharField(max_length = 100)
    desc        = models.TextField(null = True)
    button_text = models.CharField(max_length = 50, null = True)
    img_back    = models.URLField(max_length = 2000, null = True)
    img_icon    = models.URLField(max_length = 2000, null = True)

    class Meta:
        db_table = 'passports'

class HouseQuestion(models.Model):
    question   = models.CharField(max_length = 200)
    img_center = models.URLField(max_length = 2000, null = True)

    class Meta:
        db_table = 'house_questions'

class HouseChoice(models.Model):
    choice   = models.CharField(max_length = 200)
    img      = models.URLField(max_length = 2000, null = True)
    question = models.ForeignKey(HouseQuestion, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'house_choices'

class HouseResult(models.Model):
    name           = models.CharField(max_length = 50)
    img_icon       = models.TextField(null = True)
    img_bg         = models.URLField(max_length = 2000, null = True)
    tag_line       = models.CharField(max_length = 50, null = True)
    intro          = models.CharField(max_length = 500, null = True)
    share_img_icon = models.TextField(null = True)
    share_img_bg   = models.TextField(null = True)
    person_img_bg  = models.TextField(null = True)
    person1_name   = models.TextField(null = True)
    person1_img    = models.TextField(null = True)
    person2_name   = models.TextField(null = True)
    person2_img    = models.TextField(null = True)
    person3_name   = models.TextField(null = True)
    person3_img    = models.TextField(null = True)
    message        = models.TextField(null = True)
    quotes         = models.CharField(max_length = 200, null = True)

    class Meta:
        db_table = 'house_results'

class HouseFomula(models.Model):
    result    = models.ForeignKey(HouseResult, on_delete = models.SET_NULL, null = True)
    question1 = models.ForeignKey(
        HouseChoice,
        related_name = 'moonstar_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question2 = models.ForeignKey(
        HouseChoice,
        related_name = 'pet_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question3 = models.ForeignKey(
        HouseChoice,
        related_name = 'toad_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question4 = models.ForeignKey(
        HouseChoice,
        related_name = 'known_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question5 = models.ForeignKey(
        HouseChoice,
        related_name = 'expect_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question6 = models.ForeignKey(
        HouseChoice,
        related_name = 'nightmare_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question7 = models.ForeignKey(
        HouseChoice,
        related_name = 'ratherbe_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question8 = models.ForeignKey(
        HouseChoice,
        related_name = 'openbox_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question9 = models.ForeignKey(
        HouseChoice,
        related_name = 'leftright_question',
        on_delete    = models.SET_NULL,
        null         = True)

    class Meta:
        db_table = 'house_fomulas'

class WandQuestion(models.Model):
    question = models.CharField(max_length = 200)
    img_back = models.URLField(max_length = 2000, null = True)

    class Meta:
        db_table = 'wand_questions'

class WandChoice(models.Model):
    choice   = models.CharField(max_length = 200)
    question = models.ForeignKey(WandQuestion, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'wand_choices'

class WandResult(models.Model):
    name = models.CharField(max_length = 50)
    img  = models.URLField(max_length = 2000, null = True)

    class Meta:
        db_table = 'wand_results'

class WandFomula(models.Model):
    result = models.ForeignKey(WandResult, on_delete = models.SET_NULL, null = True)
    question1 = models.ForeignKey(
        WandChoice,
        related_name = 'describe_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question2 = models.ForeignKey(
        WandChoice,
        related_name = 'eyes_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question3 = models.ForeignKey(
        WandChoice,
        related_name = 'bornday_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question4 = models.ForeignKey(
        WandChoice,
        related_name = 'pride_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question5 = models.ForeignKey(
        WandChoice,
        related_name = 'travel_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question6 = models.ForeignKey(
        WandChoice,
        related_name = 'fear_question',
        on_delete    = models.SET_NULL,
        null         = True)
    question7 = models.ForeignKey(
        WandChoice,
        related_name = 'artefact_question',
        on_delete    = models.SET_NULL,
        null         = True)

    class Meta:
        db_table = 'wand_fomulas'

class FavouriteSection(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'favourite_sections'

class FavouriteChoice(models.Model):
    name    = models.CharField(max_length = 50)
    section = models.ForeignKey(FavouriteSection, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'favourite_choices'
