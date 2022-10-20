# Generated by Django 4.1.1 on 2022-09-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_order_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Processing', 'Processing')], max_length=200, null=True),
        ),
    ]
