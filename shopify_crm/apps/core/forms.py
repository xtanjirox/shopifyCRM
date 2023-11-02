from django import forms
from apps.core import models


class ProductCreateForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = models.Product
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'] = forms.CharField()
        self.fields['title'].required = True
        self.fields['title'].widget.attrs.update({"class": "form-control form-control",
                                                  "id": "deffdsfdsk dfskfmds fmlsdkf mlksdf  mlkf lmkdf slmk mlksdf "
                                                        "lmksdf ezk aultInput"})
