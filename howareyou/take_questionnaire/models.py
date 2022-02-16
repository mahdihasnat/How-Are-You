from django.db import models

# Create your models here.


ID_LENGTH = 15

'''Test'''


class Question(models.Model):
    id = models.CharField("unique id to every question",
                          max_length=ID_LENGTH, primary_key=True)

    def str(self):
        return self.id
