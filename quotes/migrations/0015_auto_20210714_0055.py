# Generated by Django 3.2.4 on 2021-07-14 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0014_rename_q_addepted_quote_q_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openorder',
            name='id',
        ),
        migrations.AlterField(
            model_name='openorder',
            name='q_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
