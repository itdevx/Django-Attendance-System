# Generated by Django 4.1 on 2022-09-28 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Student.classroom'),
            preserve_default=False,
        ),
    ]