from django.contrib import admin

from .models import Psychiatrist
from .models import ReviewBoardMember
from .models import Award
from .models import PsychiatristAward
from .models import Degree
from .models import PsychiatristDegree
from .models import Expertise
from .models import PsychiatristExpertise


# Register your models here.

class PsychiatristAwardInline(admin.TabularInline):
	model = PsychiatristAward
	extra = 1

class PsychiatristDegreeInline(admin.TabularInline):
	model = PsychiatristDegree
	extra = 1

class PsychiatristExpertiseInline(admin.TabularInline):
	model = PsychiatristExpertise
	extra = 1

class PsychiatristAdmin(admin.ModelAdmin):
	inlines = [PsychiatristAwardInline, PsychiatristDegreeInline, PsychiatristExpertiseInline]


admin.site.register(Psychiatrist,PsychiatristAdmin)
admin.site.register(ReviewBoardMember,PsychiatristAdmin)
admin.site.register(Award)
admin.site.register(Degree)
admin.site.register(Expertise)