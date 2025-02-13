from django.contrib import admin
from futbol.models import *
# Register your models here.


admin.site.register(Lliga)
admin.site.register(Equip)
admin.site.register(Jugador)

class EventInline(admin.TabularInline):
    model = Event
    extra = 2
    
class PartitAdmin(admin.ModelAdmin):
    list_display = ("equip_local", "equip_visitant","data","gols_local","gols_visitant")
    inlines = [EventInline]

admin.site.register(Partit,PartitAdmin)