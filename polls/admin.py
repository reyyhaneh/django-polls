from django.contrib import admin

from .models import Question, Choice


# customizing how the admin form looks and works by following this pattern:
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3




# 1 - creating a ModelAdmin class
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes":["colapse"]}),
        # the first element of each tuple is the title of the fieldset.
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    
    # # only allow superusers to view the question model.
    # def has_module_permission(self, request):
    #     return super().has_module_permission(request)
    

    # this tells django that Choice objects are edited on the Question page.



# 2 - pass the class the second argument to admin.site.register()
admin.site.register(Question, QuestionAdmin)


# 3 - these changes indicate how the admin models are displayed.
