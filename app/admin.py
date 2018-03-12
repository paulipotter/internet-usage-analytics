from django.contrib import admin
from .models import SocialMedia, AgeGroup, Gender, NewsSource, Device
from .models import TrustLevel, Department, BinaryEntry, Recurrence, PC
from .models import ScamType, City, Entry, SmartphoneRecurrence, LaptopRecurrence
from .models import PCRecurrence, Scam, Smartphone, Cellphone, Tablet, Laptop

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ()

class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ()

class GenderAdmin(admin.ModelAdmin):
    list_display = ()

class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ()

class DeviceAdmin(admin.ModelAdmin):
    list_display = ()

class TrustLevelAdmin(admin.ModelAdmin):
    list_display = ()

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ()

class BinaryEntryAdmin(admin.ModelAdmin):
    list_display = ()

class RecurrenceAdmin(admin.ModelAdmin):
    list_display = ()

class ScamTypeAdmin(admin.ModelAdmin):
    list_display = ()

class CityAdmin(admin.ModelAdmin):
    list_display = ()


class EntryAdmin(admin.ModelAdmin):
    list_display = ()


class SmartphoneRecurrenceAdmin(admin.ModelAdmin):
    list_display = ()

class LaptopRecurrenceAdmin(admin.ModelAdmin):
    list_display = ()

class PCRecurrenceAdmin(admin.ModelAdmin):
    list_display = ()

class ScamAdmin(admin.ModelAdmin):
    list_display = ()

class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ()

class CellphoneAdmin(admin.ModelAdmin):
    list_display = ()

class TabletAdmin(admin.ModelAdmin):
    list_display = ()

class LaptopAdmin(admin.ModelAdmin):
    list_display = ()

class PCAdmin(admin.ModelAdmin):
    list_display = ()

# Register your models here.



admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(NewsSource, NewsSourceAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(TrustLevel, TrustLevelAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(BinaryEntry, BinaryEntryAdmin)
admin.site.register(Recurrence, RecurrenceAdmin)
admin.site.register(ScamType, ScamTypeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(SmartphoneRecurrence, SmartphoneRecurrenceAdmin)
admin.site.register(LaptopRecurrence, LaptopRecurrenceAdmin)
admin.site.register(PCRecurrence, PCRecurrenceAdmin)
admin.site.register(Scam, ScamAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Cellphone, CellphoneAdmin)
admin.site.register(Tablet, TabletAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(PC, PCAdmin)
