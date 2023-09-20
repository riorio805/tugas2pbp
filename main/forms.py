from django.forms import ModelForm
from django.forms.widgets import NumberInput
from main.models import Item

class RangeInput(NumberInput):
    input_type = "range"
    template_name = "range.html"

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "rarity", "effect", "image_dir"]
        widgets = {"rarity": RangeInput(attrs={
            "min": 1,
            "max": 5,
            "oninput": "rarityVal.value = this.value",
            "list": "number"})}