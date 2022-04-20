from django.contrib import admin

from bus import models


admin.site.register(models.Bus)
admin.site.register(models.Ticket)