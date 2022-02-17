from django.db import models
from django.utils.translation import gettext_lazy

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
    # do we need id ?
    # id = models.CharField("unique id to every question",
    #                       max_length=ID_LENGTH, primary_key=True)

    # added_by = models.ForeignKey(Psychiatrist)
    # should we not have a string type question
    class QuestionType(models.TextChoices):
        RADIO = 'RD', gettext_lazy('Radio')
        SLIDER = 'SL', gettext_lazy('Number Slider')
        MUL_CHOICE = 'CH', gettext_lazy('Multiple Choice')

    type = models.CharField(max_length=2, choices=QuestionType.choices, default=QuestionType.RADIO)

    def str(self):
        return self.id
