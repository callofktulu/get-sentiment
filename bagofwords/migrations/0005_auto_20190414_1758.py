# Generated by Django 2.1.7 on 2019-04-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bagofwords', '0004_auto_20190414_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentiment',
            name='negativity',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='sentiment',
            name='objectivity',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='sentiment',
            name='polarity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sentiment',
            name='positivity',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]