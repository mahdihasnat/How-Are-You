from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

# Create your models here.
from psychiatrists.models import Psychiatrist

ID_LENGTH = 15
FIELD_LENGTH = 20
TEXT_FIELD = 1000
CHOICE_LENGTH = 5
UNSPECIFIED = 'unspecified'


class Status(models.TextChoices):
    # pass
    PENDING_APPROVAL = 'P_AP', gettext_lazy('Pending Approval')
    IN_USE = 'USE', gettext_lazy('Being Used')
    PENDING_DISAPPROVAL = 'P_DP', gettext_lazy('Pending Removal')
    ARCHIVED = 'ARC', gettext_lazy('Archived')


# -question_id : int

# -added_by : Psychiatrist
# -type : string
# -created_at : datetime
# -question_text : string
# -options : list()
# - status : char


class Question(models.Model):
    # do we need id ?
    # id = models.CharField("unique id to every question",
    #                       max_length=ID_LENGTH, primary_key=True)

    added_by = models.ForeignKey(Psychiatrist, on_delete=models.DO_NOTHING)

    # should we not have a string type question
    class QuestionType(models.TextChoices):
        RADIO = 'RD', gettext_lazy('Radio')
        SLIDER = 'SL', gettext_lazy('Number Slider')
        MUL_CHOICE = 'CH', gettext_lazy('Multiple Choice')

    type = models.CharField(max_length=2, choices=QuestionType.choices, default=QuestionType.RADIO)

    created_at = models.DateTimeField(default=timezone.now)
    # added by me
    changed_at = models.DateTimeField(default=timezone.now)

    question_text = models.CharField(max_length=TEXT_FIELD, null=False, blank=False, default=UNSPECIFIED)

    # class QuestionStatus(models.TextChoices):
    #     PENDING_APPROVAL = 'P_AP', gettext_lazy('Pending Approval')
    #     IN_USE = 'USE', gettext_lazy('Being Used')
    #     PENDING_DISAPPROVAL = 'P_DP', gettext_lazy('Pending Removal')

    # def str(self):
    #     return self


# class Anser


class Option(models.Model):
    # not adding id
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=FIELD_LENGTH, null=False, blank=False, default=UNSPECIFIED)


class Rule(models.Model):
    # id ignored
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE)
    rubric_score = models.FloatField(default=0)
    _from = models.DateTimeField(default=timezone.now)
    _end = models.DateTimeField(default=timezone.now)


class Test(models.Model):
    # id ignored
    # should it be ReviewBoardMember
    added_by = models.ForeignKey(Psychiatrist, on_delete=models.DO_NOTHING)
    # disease_id = models.ForeignKey(Disease)
    name = models.CharField("Name of the test", max_length=FIELD_LENGTH, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.CharField(max_length=CHOICE_LENGTH, choices=Status.choices, default=Status.PENDING_APPROVAL)
    questions = models.ManyToManyField(Question,through='TestQuestion')

class TestQuestion(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_pending = models.CharField(
        "the relation between test and the qeustion",
        max_length=CHOICE_LENGTH,
        choices=Status.choices,
        default=Status.PENDING_APPROVAL
    )

