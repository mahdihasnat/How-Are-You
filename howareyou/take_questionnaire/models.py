from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

# Create your models here.
# from howareyou.psychiatrists.models import Psychiatrist

ID_LENGTH = 15
FIELD_LENGTH = 20
TEXT_FIELD = 1000
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

    created_at = models.DateTimeField(default=timezone.now)
    # added by me
    changed_at = models.DateTimeField(default=timezone.now)

    question_text = models.CharField(max_length=TEXT_FIELD)

    class QuestionStatus(models.TextChoices):
        pass

    # def str(self):
    #     return self
