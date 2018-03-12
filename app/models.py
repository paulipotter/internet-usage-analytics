from django.db import models
from django.conf import settings


class SocialMedia(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class AgeGroup(models.Model):
    key = models.IntegerField(primary_key=True)
    group = models.CharField(max_length=20)


class Gender(models.Model):
    key = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=20)


class NewsSource(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class Device(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class TrustLevel(models.Model):
    key = models.IntegerField(primary_key=True)
    level = models.CharField(max_length=20)


class Department(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class BinaryEntry(models.Model):
    key = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=20)


class Recurrence(models.Model):
    key = models.IntegerField(primary_key=True)
    recurrence = models.CharField(max_length=20)


class ScamType(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class City(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)


class Entry(models.Model):
    entry_id = models.IntegerField(primary_key=True)
    household_size = models.IntegerField()
    age = models.IntegerField()
    city = models.OneToOneField(City, on_delete=models.PROTECT)
    social_media = models.OneToOneField(SocialMedia, on_delete=models.PROTECT)
    news_source = models.OneToOneField(NewsSource, on_delete=models.PROTECT)
    internet_trust = models.OneToOneField(TrustLevel, on_delete=models.PROTECT)
    preferred_device = models.OneToOneField(Device, on_delete=models.PROTECT)
    gender = models.OneToOneField(Gender, on_delete=models.PROTECT)


class SmartphoneRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    key = models.IntegerField()  # recurrence id


class LaptopRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    key = models.IntegerField()


class PCRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    key = models.IntegerField()


class Scam(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    reported = models.ForeignKey(BinaryEntry, on_delete=models.PROTECT)
    scam_type = models.ForeignKey(ScamType, on_delete=models.PROTECT)


class Smartphone(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='smartphone_use')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='smartphone_home')


class Cellphone(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='cellphone_use')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='cellphone_home')


class Tablet(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='tablet_use')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='tablet_home')


class Laptop(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='laptop_use')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='laptop_home')


class PC(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='pc_use')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='pc_home')
