# Generated by Django 3.0.3 on 2020-03-20 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sorting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(null=True)),
                ('is_send_newsletter', models.BooleanField(null=True)),
                ('google_id', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserWand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
                ('wand_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sorting.WandResult')),
            ],
            options={
                'db_table': 'user_wands',
            },
        ),
        migrations.CreateModel(
            name='UserHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sorting.HouseResult')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'user_houses',
            },
        ),
        migrations.CreateModel(
            name='UserFavourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sorting.FavouriteChoice')),
                ('favourite_section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sorting.FavouriteSection')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
        ),
    ]
