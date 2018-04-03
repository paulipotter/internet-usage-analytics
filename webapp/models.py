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
    department = models.ForeignKey(Department,
                            on_delete=models.PROTECT)


class Entry(models.Model):
    entry_id = models.IntegerField(primary_key=True)
    household_size = models.IntegerField()
    age = models.IntegerField()
    city = models.ForeignKey(City,
                    on_delete=models.PROTECT)
    social_media = models.ForeignKey(SocialMedia,
                    on_delete=models.PROTECT)
    news_source = models.ForeignKey(NewsSource,
                    on_delete=models.PROTECT)
    internet_trust = models.ForeignKey(TrustLevel,
                    on_delete=models.PROTECT)
    preferred_device = models.ForeignKey(Device,
                    on_delete=models.PROTECT)
    gender = models.ForeignKey(Gender,
                    on_delete=models.PROTECT)


class SmartphoneRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    key = models.ForeignKey(Recurrence,
                on_delete=models.PROTECT)  # recurrence id


class LaptopRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    key = models.ForeignKey(Recurrence,
                on_delete=models.PROTECT)  # recurrence id


class PCRecurrence(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT)  # Entry
    key = models.ForeignKey(Recurrence,
                on_delete=models.PROTECT)  # recurrence id


class Scam(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT,
                db_column='entry_id')  # Entry
    reported = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                db_column='reported')
    scam_type = models.ForeignKey(ScamType,
                on_delete=models.PROTECT,
                db_column='scam_type')


class Smartphone(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT,
                db_column='entry_id')  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='smartphone_use',
                db_column='utilize')
    home = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='smartphone_home',
                db_column='home')


class Cellphone(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT,
                db_column='entry_id')  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='cellphone_use',
                db_column='utilize')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='cellphone_home',
            db_column='home')


class Tablet(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT,
                db_column='entry_id')  # Entry
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='tablet_use',
                db_column='utilize')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='tablet_home',
            db_column='home')


class Laptop(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT,
                db_column='entry_id')
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='laptop_use',
                db_column='utilize')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='laptop_home',
            db_column='home')


class PC(models.Model):
    entry_id = models.OneToOneField(Entry,
                primary_key=True,
                on_delete=models.PROTECT,
                db_column='entry_id')
    quantity = models.IntegerField()
    utilize = models.ForeignKey(BinaryEntry,
                on_delete=models.PROTECT,
                related_name='pc_use',
                db_column='utilize')
    home = models.ForeignKey(BinaryEntry,
            on_delete=models.PROTECT,
            related_name='pc_home',
            db_column='home')
