import random

from patients.models import Patient
from psychiatrists.models import Psychiatrist
from take_questionnaire.models import Test, Question, Option, Rule, TestQuestion

Patient.objects.all().delete()
Psychiatrist.objects.all().delete()
Test.objects.all().delete()

Option.objects.all().delete()
Question.objects.all().delete()
Rule.objects.all().delete()
# .objects.all().delete()


PSYC_COUNT = 1
PAT_COUNT = 3
# if __name__ != '__main__':
# print("inside main")
moderator = None
while PSYC_COUNT > 0:
    psy = Psychiatrist(
        verified=True,
        available_times="4pm-10pm",
        # awards=None,
        username='psy_' + str(PSYC_COUNT),
        name='psy_' + str(PSYC_COUNT),
        password='.',
        email='psy' + str(PSYC_COUNT) + '@abc.com',
        mobile_number='123'
    )
    psy.save()
    moderator = psy
    PSYC_COUNT = PSYC_COUNT - 1

while PAT_COUNT > 0:
    pat = Patient(
        username='pat_' + str(PAT_COUNT),
        name='pat_' + str(PAT_COUNT),
        password='.',
        email='pat' + str(PAT_COUNT) + '@abc.com',
        mobile_number='123',
        height=120 + min(45, PAT_COUNT * random.randint(0, 10)),
        weight=45 + min(50, PAT_COUNT * random.randint(0, 10)),
        info='Patient no ' + str(PAT_COUNT)
    )
    pat.save()
    PAT_COUNT = PAT_COUNT - 1

# General Test
test = Test(
    added_by=moderator,
    name='General',
    is_approved='USE'
)

test.save()

QUESTION_COUNT = 5
questions = [
    'I felt worthless.',
    'I felt that I had nothing to look forward to.',
    'I felt helpless.',
    'I felt sad.',
    'I felt like a failure.',
]

OPTION_COUNT = 5
options = [
    ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
    ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
    ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
    ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
    ['Never', 'Rarely', 'Sometimes', 'Often', 'Always']
]

weights = [
    [0, .1, .2, .3, .4],
    [0, .1, .2, .3, .4],
    [0, .1, .2, .3, .4],
    [0, .1, .2, .3, .4],
    [0, .1, .2, .3, .4],
]

for i in range(QUESTION_COUNT):
    # Question
    ques = Question(
        added_by=moderator,
        type='CH',
        question_text=questions[i]
    )
    ques.save()

    for opt in range(OPTION_COUNT):
        option = Option(
            question_id=ques,
            text=options[i][opt]
        )
        option.save()

        rule = Rule(
            option_id=option,
            question_id=ques,
            rubric_score=weights[i][opt],
        )
        rule.save()

    test_ques = TestQuestion(
        test_id=test,
        question_id=ques,
        is_pending='USE'
    )
    test_ques.save()
