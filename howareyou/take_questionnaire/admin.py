# Register your models here.
from django.contrib import admin

from .models import Option
from .models import Question, Test, TestQuestion
from .models import Rule

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Rule)


class TestQuestionInline(admin.TabularInline):
	model = TestQuestion;
	extra = 1

class TestAdmin(admin.ModelAdmin):
	inlines = [TestQuestionInline,]

admin.site.register(Test,TestAdmin)