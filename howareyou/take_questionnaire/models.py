from django.db import models

# Create your models here.


ID_LENGTH = 15
FIELD_LENGTH = 20
UNSPECIFIED = 'unspecified'


# -question_id : int
# -type : string
# -added_by : Psychiatrist
# -created_at : datetime
# -question_text : string
# -options : list()
# - status : char


class Question(models.Model):
    id = models.CharField("unique id to every question",
                          max_length=ID_LENGTH, primary_key=True)
    type = models.CharField(max_length=FIELD_LENGTH, default=UNSPECIFIED)

    def str(self):
        return self.id
