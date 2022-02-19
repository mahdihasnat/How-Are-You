from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

from patients.models import Patient
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

    added_by = models.ForeignKey(Psychiatrist, on_delete=models.CASCADE)

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
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, parent_link=True)
    text = models.CharField(max_length=FIELD_LENGTH, null=False, blank=False, default=UNSPECIFIED)


class Rule(models.Model):
    # id ignored
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE)
    rubric_score = models.IntegerField(default=0)
    _from = models.DateTimeField(default=timezone.now)
    # should end be the current time
    _end = models.DateTimeField(default=timezone.datetime.max)


class Test(models.Model):
    # id ignored
    # should it be ReviewBoardMember
    added_by = models.ForeignKey(Psychiatrist, on_delete=models.DO_NOTHING)
    # disease_id = models.ForeignKey(Disease)
    name = models.CharField("Name of the test", max_length=FIELD_LENGTH, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.CharField(max_length=CHOICE_LENGTH, choices=Status.choices, default=Status.PENDING_APPROVAL)
    questions = models.ManyToManyField(Question, through='TestQuestion')


class TestQuestion(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_pending = models.CharField(
        "the relation between test and the qeustion",
        max_length=CHOICE_LENGTH,
        choices=Status.choices,
        default=Status.PENDING_APPROVAL
    )


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    verifier = models.ForeignKey(Psychiatrist, on_delete=models.SET_NULL, null=True, default=None)
    questions = models.ManyToManyField(Question, through='Answer')
    submission_time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(default='')

    def sum_score(self):
        score = 0
        # iterate over through filed of answers
        for question in self.questions.all():
            answer = Answer.objects.get(testresult=self, question=question)
            score += answer.score
        if score < 17:
            return 'None to slight'
        elif score < 23:
            return 'Mild'
        elif score < 33:
            return 'Moderate'
        else:
            return 'Severe'


class Answer(models.Model):
    testresult = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.IntegerField(null=False, blank=False)
    score = models.IntegerField(default=0)
