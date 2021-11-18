from django.contrib import admin

# Register your models here.
from .models import Question
admin.site.register(Question)

from .models import UserAccount
admin.site.register(UserAccount)

from .models import Comment
admin.site.register(Comment)
