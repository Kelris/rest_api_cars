from django.contrib import admin

# Register your models here.
from .models import Car, Vote


class VoteInLine(admin.StackedInline):
    model = Vote
    extra = 0


class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['make_name']}),
        (None, {'fields': ['model_name']}),
    ]
    inlines = [VoteInLine]


admin.site.register(Car, CarAdmin)
