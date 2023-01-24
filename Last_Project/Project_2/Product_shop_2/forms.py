from django import forms


class CardForms(forms.Form):
    count_all = forms.IntegerField(label="Count:", required=False, min_value=1)
    name = forms.CharField(label="name", max_length=100)
    category = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=7, decimal_places=2)
    description = forms.CharField(max_length=100)
    icon = forms.ImageField()
    name_unit = forms.CharField(max_length=50)
    base64 = forms.TextInput()

    def __init__(self, request, *args, **kwargs):
        super(CardForms, self).__init__(*args, **kwargs)
        self.initial['count_all'] = 1
