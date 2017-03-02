from django import forms

from .models import Post
from .models import Contact

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('baslik', 'yazi',)
class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields=('isim','mail','telefon','mesaj',)