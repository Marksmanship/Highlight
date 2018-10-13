from django.contrib import admin
from .models import (
	School,
	Sport,
	School_Sport,
	User_School,
	User_Sport,
	Sport_Stat,
)
# Register your models here.
admin.site.register(School)
admin.site.register(Sport)
admin.site.register(School_Sport)
admin.site.register(User_School)
admin.site.register(User_Sport)
admin.site.register(Sport_Stat)
