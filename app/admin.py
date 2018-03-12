from django.contrib import admin
from .models import SocialMedia, AgeGroup, Gender, NewsSource, Device
from .models import TrustLevel, Department, BinaryEntry, Recurrence, PC
from .models import ScamType, City, Entry, SmartphoneRecurrence, LaptopRecurrence
from .models import PCRecurrence, Scam, Smartphone, Cellphone, Tablet, Laptop

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ()

class AgeGroupAdmin(admin.ModelAdmin):

class GenderAdmin(admin.ModelAdmin):

class NewsSourceAdmin(admin.ModelAdmin):

class DeviceAdmin(admin.ModelAdmin):


class TrustLevelAdmin(admin.ModelAdmin):

class DepartmentAdmin(admin.ModelAdmin):

class BinaryEntryAdmin(admin.ModelAdmin):

class RecurrenceAdmin(admin.ModelAdmin):

class ScamTypeAdmin(admin.ModelAdmin):

class CityAdmin(admin.ModelAdmin):


class EntryAdmin(admin.ModelAdmin):


class SmartphoneRecurrenceAdmin(admin.ModelAdmin):

class LaptopRecurrenceAdmin(admin.ModelAdmin):

class PCRecurrenceAdmin(admin.ModelAdmin):

class ScamAdmin(admin.ModelAdmin):

class SmartphoneAdmin(admin.ModelAdmin):

class CellphoneAdmin(admin.ModelAdmin):

class TabletAdmin(admin.ModelAdmin):

class LaptopAdmin(admin.ModelAdmin):

class PCAdmin(admin.ModelAdmin):

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
