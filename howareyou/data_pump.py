from psychiatrists.models import Psychiatrist

# if __name__ != '__main__':
# print("inside main")
psy = Psychiatrist(
    verified=True,
    available_times="4pm-10pm",
    # awards=None,
    username='psy_1',
    name='psy_1',
    password='.',
    email='p@abc.com',
    mobile_number='123'
)
psy.save()
# print(psy)
# q = Question()
