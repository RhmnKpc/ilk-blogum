from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post (models.Model):
    yazar=models.ForeignKey('auth.User')
    baslik=models.CharField(max_length=200)
    yazi=RichTextField()
    yaratilis_tarihi=models.DateTimeField(default=timezone.now())
    yayin_tarihi=models.DateTimeField(blank=True,null=True)

    def yayinla(self):
        self.yayin_tarihi=timezone.now()
        self.save()

    def __str__(self):
        return self.baslik

class Contact(models.Model):
    isim=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    telefon=models.CharField(max_length=20)
    mesaj=models.TextField()
    tarih=models.DateTimeField(default=timezone.now())

    def gonder(self):
        self.tarih=timezone.now()
        self.save()

    def __str__(self):
        return self.isim