from django.contrib import admin
from .models import User, Category, Question, Answer, RecruiterMessage, Role, Permission

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(RecruiterMessage)
admin.site.register(Role)
admin.site.register(Permission)
