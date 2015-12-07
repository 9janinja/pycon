from django.contrib import admin
from collection.models import Join
# Register your models here.
#from .models import Join


class JoinAdmin(admin.ModelAdmin):
	list_display = ['__str__','timestamp','updated']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)