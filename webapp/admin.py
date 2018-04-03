from django.contrib import admin
from .models import SocialMedia, AgeGroup, Gender, NewsSource, Device
from .models import TrustLevel, Department, BinaryEntry, Recurrence, PC
from .models import ScamType, City, Entry, SmartphoneRecurrence, LaptopRecurrence
from .models import PCRecurrence, Scam, Smartphone, Cellphone, Tablet, Laptop

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ('group',)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)

class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TrustLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('key', 'name')

class BinaryEntryAdmin(admin.ModelAdmin):
    list_display = ('answer',)

class RecurrenceAdmin(admin.ModelAdmin):
    list_display = ('recurrence',)

class ScamTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'household_size', 'age', 'city', 'social_media',
    'news_source', 'internet_trust', 'preferred_device', 'gender')


class SmartphoneRecurrenceAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'key')

class LaptopRecurrenceAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'key')

class PCRecurrenceAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'key')

class ScamAdmin(admin.ModelAdmin):
    list_display = ('reported', 'scam_type')

class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'quantity', 'utilize', 'home')

class CellphoneAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'quantity', 'utilize', 'home')

class TabletAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'quantity', 'utilize', 'home')

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'quantity', 'utilize', 'home')

class PCAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'quantity', 'utilize', 'home')

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
