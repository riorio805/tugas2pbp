from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from inventory.settings import ALLOWED_FILES
import requests
import re
exts = '|'.join(ALLOWED_FILES)

# Create your models here.
def validate_image_url(value):
    # check url has a downloadable file
    try:
        r = requests.get(value, timeout=1)
    except requests.exceptions.RequestException as e:
        print(e)
        raise ValidationError(u'URL doesn\'t exist or isn\'t available currently.')
    
    print(r.headers['Content-Type'])

    if re.match(f"image/({exts})", r.headers['content-type']) == None:
        raise ValidationError(u'Wrong file type.')

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    rarity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    effect = models.TextField()
    image_dir = models.URLField(validators=[URLValidator(), validate_image_url])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
