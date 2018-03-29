from django.db import models
from django.conf import settings


class SocialMedia(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class AgeGroup(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class Gender(models.Model):
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


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
    department = models.ForeignKey(Department)


class Entry(models.Model):
    entry_id = models.IntegerField(primary_key=True)
    household_size = models.IntegerField()
    age = models.IntegerField()
    city = models.OneToOneField(City)
    social_media = models.OneToOneField(SocialMedia)
    news_source = models.OneToOneField(NewsSource)
    internet_trust = models.OneToOneField(TrustLevel)
    preferred_device = OneToOneField.ForeignKey(Devices)
    gender = models.OneToOneField(Gender)


class SmartphoneRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)  # Entry
    key = models.IntegerField()  # recurrence id


class LaptopRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)  # Entry
    key = models.IntegerField()


class PCRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)  # Entry
    key = models.IntegerField()


class Scam(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)  # Entry
    reported = models.ForeignKey(BinaryEntry)
    scam_type = models.ForeignKey(ScamType)


class Smartphone(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry)
    home = models.ForeignKey(BinaryEntry)


class Cellphone(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry)
    home = models.ForeignKey(BinaryEntry)


class Tablet(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry)
    home = models.ForeignKey(BinaryEntry)


class Laptop(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry)
    home = models.ForeignKey(BinaryEntry)


class PC(models.Model):
    entry_id = models.OneToOneField(Entry, primary_key=True)
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry)
    home = models.ForeignKey(BinaryEntry)
