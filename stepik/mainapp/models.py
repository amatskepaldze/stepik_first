from django.db import models
from django.contrib.auth.models import User
import datetime

class Dictionary(models.Model):
    original = models.CharField(max_length=50)
    translate = models.CharField(max_length=50)
    comment = models.TextField(max_length=250)
    pushed_data = models.DateTimeField(auto_now=True)

    def add_new_word(self, english, russian, comments):
        self.original = english
        self.translate = russian
        self.comment = comments
        self.pushed_data = datetime.datetime.now()
        self.save()

    def make_changes(self, dictionary):
        for key, value in dictionary.items():
            if key != 'csrfmiddlewaretoken':
                setattr(self, key, value[0])
                print(getattr(self, key))
        self.pushed_data = datetime.datetime.now()
        self.save()



