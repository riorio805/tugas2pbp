# Generated by Django 4.2.5 on 2023-09-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_effect_item_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_dir',
            field=models.TextField(default='main/images/March_7th_Sticker_07.png'),
            preserve_default=False,
        ),
    ]