from django.contrib import admin
from .models import (
	Schools,
	Sports,
	School_Sports,
	User_Schools,
	User_Sports,
	Sport_Stats,
)
# Register your models here.
admin.site.register(Schools)
admin.site.register(Sports)
admin.site.register(School_Sports)
admin.site.register(User_Schools)
admin.site.register(User_Sports)
admin.site.register(Sport_Stats)
