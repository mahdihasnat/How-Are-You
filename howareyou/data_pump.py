import random

from patients.models import Patient
from psychiatrists.models import Psychiatrist
from take_questionnaire.models import Test, Question, Option, Rule, TestQuestion, Dieases

Psychiatrist.objects.all().delete()
Test.objects.all().delete()

Option.objects.all().delete()
Question.objects.all().delete()
Rule.objects.all().delete()
# .objects.all().delete()
Patient.objects.all().delete()

PSYC_COUNT = 5
psycs = ["Dr. Habibur Rahman", "Dr. Nargis Khanam", "Dr. Hakim Sheikh", "Dr. Jony Ul Islam",
         "Dr. Hasanul Banna"]
PAT_COUNT = 3
pats = ["nayem", "tanvir", "noman"]

assert PSYC_COUNT == len(psycs)
assert PAT_COUNT == len(pats)
# if __name__ != '__main__':
# print("inside main")
moderator = None
while PSYC_COUNT > 0:
    psy = Psychiatrist(
        verified=True,
        available_times="4pm-10pm",
        # awards=None,
        username='psy_' + str(PSYC_COUNT),
        name=psycs[PSYC_COUNT - 1],
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
        name=pats[PAT_COUNT - 1],
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
def adult_test(moderator):
    test = Test(
        added_by=moderator,
        is_approved='USE',

        name='LEVEL 2—Depression—Adult (PROMIS Emotional Distress—Depression—Short Form)',
        details_gimmic='Are you depressed for any recent happenings aroung you? ',

        instruction='On the DSM-5 Level 1 cross-cutting questionnaire that you just completed, you indicated that during the past 2'
                    'weeks you (the individual receiving care) have been bothered by “no interest or pleasure in doing things” and'
                    '/or “feeling down, depressed, or hopeless” at a mild or greater level of severity. '
                    'The questions below ask about these feelings in more detail and especially how often you (the individual receiving care) '
                    'have been bothered by a list of symptoms during the past 7 days.',

        details_duration='In the past SEVEN (7) DAYS....',
        has_score=True,

    )

    test.save()

    QUESTION_COUNT = 8
    questions = [
        'I felt worthless.',
        'I felt that I had nothing to look forward to.',
        'I felt helpless.',
        'I felt sad.',
        'I felt like a failure.',
        'I felt depressed.',
        'I felt unhappy.',
        'I felt hopeless.',
    ]

    OPTION_COUNT = 5

    options = [
        ['None', 'Rarely', 'Sometimes', 'Often', 'Always'],
        ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
        ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
        ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
        ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
        ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
        ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
        ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'],

    ]

    weights = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]

    assert len(questions) == QUESTION_COUNT
    assert len(weights) == QUESTION_COUNT
    assert len(weights) == QUESTION_COUNT
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


def general_test(moderator):
    test = Test(
        added_by=moderator,
        # name='DSM-5 Self-Rated Level 1 Cross-Cutting Symptom Measure—Adult',
        is_approved='USE',
        details_gimmic='Take a quick tour to the DSM Questionnaire to discover your current mental health condition.',

        name='DSM-5 Self-Rated Level 1 Cross-Cutting Symptom Measure—Adult' \
             'Take some moment to go through our Depression tests.',
        instruction='The questions below ask about things that might have bothered you.' \
                    'For each question, circle the number that bestdescribes how much (or how often) you have been '
                    'bothered by' \
                    ' each problem during the past TWO (2) WEEKS.',
        details_duration='During the past TWO (2) WEEKS, how much (or how often) have you been'
                         'bothered by the following problems?',
        has_score=False,
    )

    test.save()

    QUESTION_COUNT = 13
    questions = [
        'Little interest or pleasure in doing things?',
        'Feeling more irritated, grouchy, or angry than usual?',
        'Sleeping less than usual, but still have a lot of energy?',
        'Feeling nervous, anxious, frightened, worried, or on edge?',
        'Unexplained aches and pains (e.g., head, back, joints, abdomen, legs)?',
        'Thoughts of actually hurting yourself?',
        'Hearing things other people couldn’t hear, such as voices even when no one was around?',
        'Problems with sleep that affected your sleep quality over all?',
        'Problems with memory (e.g., learning new information) or with location (e.g., finding your way home)?',
        'Unpleasant thoughts, urges, or images that repeatedly enter your mind?',
        'Feeling detached or distant from yourself, your body, your physical surroundings, or your memories?',
        'Not knowing who you really are or what you want out of life?',
        'Drinking at least 4 drinks of any kind of alcohol in a single day?',

    ]
    assert len(questions) == QUESTION_COUNT
    OPTION_COUNT = 5
    options = ['Not at all', 'Rare, less than a day or two', 'Several days', 'More than half the days',
               'Nearly every day']
    weights = [1, 2, 3, 4, 5]
    assert len(questions) == QUESTION_COUNT
    assert len(weights) == OPTION_COUNT
    assert len(weights) == OPTION_COUNT
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
                text=options[opt]
            )
            option.save()

            rule = Rule(
                option_id=option,
                question_id=ques,
                rubric_score=weights[opt],
            )
            rule.save()

        test_ques = TestQuestion(
            test_id=test,
            question_id=ques,
            is_pending='USE'
        )
        test_ques.save()


general_test(moderator)
adult_test(moderator)

diseases = ['PTSD', 'Depression', 'Orthorexia', 'OCD']
desc = ['Post Traumatic Stress Disorder', 'Depression', 'Orthorexia is an unhealthy focus on eating in a healthy way.',
        'Obsessive compulsive disorder']
DISEASE_COUNT = 4
assert DISEASE_COUNT == len(diseases)
assert len(desc) == DISEASE_COUNT
while DISEASE_COUNT > 0:
    DISEASE_COUNT -= 1
    dis = Dieases(
        reviewer=moderator,
        name=diseases[DISEASE_COUNT],
        description=desc[DISEASE_COUNT],
    )
    dis.save()
