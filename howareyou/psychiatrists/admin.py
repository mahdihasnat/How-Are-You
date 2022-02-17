from django.contrib import admin

from .models import Psychiatrist
from .models import ReviewBoardMember
from .models import Award
from .models import Degree
from .models import Expertise


# Register your models here.

admin.site.register(Psychiatrist)
admin.site.register(ReviewBoardMember)
admin.site.register(Award)
admin.site.register(Degree)
admin.site.register(Expertise)