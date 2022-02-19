# Register your models here.
from django.contrib import admin

from .models import Option
from .models import Question, Test, TestQuestion
from .models import Rule
from .models import Dieases

from .models import TestResult,Answer

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Rule)
admin.site.register(Dieases)


class TestQuestionInline(admin.TabularInline):
	model = TestQuestion;
	extra = 1

class TestAdmin(admin.ModelAdmin):
	inlines = [TestQuestionInline,]

admin.site.register(Test,TestAdmin)

class TestResultAnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

class TestResultAdmin(admin.ModelAdmin):
	inlines = [TestResultAnswerInline,]

admin.site.register(TestResult,TestResultAdmin)