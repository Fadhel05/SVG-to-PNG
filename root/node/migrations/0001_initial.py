# Generated by Django 4.0.5 on 2022-06-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'mode',
            },
        ),
    ]
