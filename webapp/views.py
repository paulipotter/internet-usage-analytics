from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from django import forms
from .models import AgeGroup, SocialMedia, Gender, NewsSource, Device, TrustLevel
from .models import Department, BinaryEntry, Recurrence, ScamType, LaptopRecurrence
from .models import PCRecurrence, SmartphoneRecurrence, Tablet, Smartphone
from .models import PC, Laptop, Cellphone, Entry, City, Scam
import ast
from django.db.models import Max, Min
from django.contrib.auth.models import User
import json
from random import uniform
#import pandas as pd


# Create your views here.
def home(request):
    print("home")
    # when "upload file" gets clicked
    # if request.method == 'POST':
    #     new_types = request.FILES['myfile']
    #     # if dict is not empty
    #     if bool(request.FILES):
    #         # get filename
    #         for fn in request.FILES:
    #             filename = request.FILES[fn].name
    #             print(filename)
    #
    #         #use pandas to read csv
    #         csv = pd.read_csv(request.FILES['myfile'])
    #         # get list of columns
    #         column = list(csv.columns.values)
    #
    #         # the database basically has 5 parts -- 3 groups of similar Tables
    #         # and 2 unique ones
    #
    #         two_col_file = ["SocialMedia.csv", "AgeGroup.csv", "Gender.csv",
    #             "NewsSource.csv", "Device.csv", "TrustLevel.csv", "Department.csv",
    #             "BinaryEntry.csv", "Recurrence.csv", "ScamType.csv"]
    #         recurrence_file = ["LaptopRecurrence.csv",
    #                            "PCRecurrence.csv", "SmartphoneRecurrence.csv"]
    #         device_file = ["Tablet.csv", "Smartphone.csv", "PC.csv",
    #                        "Laptop.csv", "Cellphone.csv"]
    #
    #         if filename in two_col_file:
    #             col1_dataframe = csv[[column[0]]]
    #             col2_dataframe = csv[[column[1]]]
    #             print(column)
    #             for value in range(csv.shape[0]):  # no. of rows to be read
    #                 command = ""
    #                 col1_value = int(col1_dataframe.at[value, column[0]])
    #                 col2_value = str(col2_dataframe.at[value, column[1]])
    #                 command = filename.split(".")[0] + ".objects.create("+column[0]+"="
    #                 command += str(col1_value) + ", " + column[1] + "=\'" + str(col2_value)+"\')"
    #                 print(command)
    #                 exec(command)
    #             messages.info(request, str(filename + " processed"))
    #
    #         elif filename == "Entry.csv":
    #             col1_dataframe = csv[[column[0]]]
    #             col2_dataframe = csv[[column[1]]]
    #             col3_dataframe = csv[[column[2]]]
    #             col4_dataframe = csv[[column[3]]]
    #             col5_dataframe = csv[[column[4]]]
    #             col6_dataframe = csv[[column[5]]]
    #             col7_dataframe = csv[[column[6]]]
    #             col8_dataframe = csv[[column[7]]]
    #             col9_dataframe = csv[[column[8]]]
    #             col10_dataframe = csv[[column[9]]]
    #
    #             for value in range(csv.shape[0]):
    #                 command = ""
    #                 col1_value = str(col1_dataframe.at[value,column[0]]) # entry_id
    #                 col2_value = str(col2_dataframe.at[value,column[1]]) # household_size
    #                 col3_value = str(col3_dataframe.at[value,column[2]]) # age
    #                 col4_value = str(col4_dataframe.at[value,column[3]]) # city
    #                 col5_value = str(col5_dataframe.at[value,column[4]]) # social_media
    #                 col6_value = str(col6_dataframe.at[value,column[5]]) # news_source
    #                 col7_value = str(col7_dataframe.at[value,column[6]]) # internet_trust
    #                 col8_value = str(col8_dataframe.at[value,column[7]]) # preferred_device
    #                 col9_value = str(col9_dataframe.at[value,column[8]]) # gender
    #                 col10_value = str(col10_dataframe.at[value,column[9]]) # age_group
    #                 Entry.objects.create(entry_id=col1_value,
    #                                      household_size=col2_value,
    #                                      age=col3_value,
    #                                      city=City.objects.get(key=col4_value),
    #                                      social_media=SocialMedia.objects.get(key=col5_value),
    #                                      news_source=NewsSource.objects.get(key=col6_value),
    #                                      internet_trust=TrustLevel.objects.get(key=col7_value),
    #                                      preferred_device=Device.objects.get(key=col8_value),
    #                                      gender=Gender.objects.get(key=col9_value),
    #                                      age_group=AgeGroup.objects.get(key=col10_value))
    #                 lin = filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value)
    #                 lin += ' ' + str(col3_value)+ ' ' + str(col4_value)+ ' ' + str(col5_value)
    #                 lin += ' ' + str(col6_value)+ ' ' + str(col7_value)+ ' ' + str(col8_value)+ ' ' + str(col9_value)
    #                 print(lin)
    #                 # command = filename.split(".")[0]+".objects.create("+column[0]+"="
    #                 # command += col1_value+","+column[1]+"="+col2_value
    #                 # command += ","+column[2]+"="+col3_value+","+column[3]+"=\'"+col4_value+"\',"+column[4]+"=\'"
    #                 # command += col5_value+"\',"+column[5]+"=\'"+col6_value+"\',"+column[6]+"=\'"
    #                 # command += col7_value+"\',"+column[7]+"=\'"+col8_value
    #                 # command += "\',"+column[8]+"=\'"+col9_value+"\')"
    #                 #
    #                 # print(command)
    #                 #exec(command)
    #
    #                 # AgeGroup.objects.get(key=col1_value).type.add(col2_value)
    #
    #         elif filename == "City.csv":
    #             col1_dataframe = csv[[column[0]]]
    #             col2_dataframe = csv[[column[1]]]
    #             col3_dataframe = csv[[column[2]]]
    #
    #             for value in range(csv.shape[0]):
    #                 command = ""
    #                 col1_value = str(col1_dataframe.at[value,column[0]]) # key
    #                 col2_value = str(col2_dataframe.at[value,column[1]]) # name
    #                 col3_value = str(col3_dataframe.at[value,column[2]]) # department
    #                 dept = Department.objects.get(key=col3_value)
    #
    #                 City.objects.create(key=col1_value,name=col2_value,department=dept)
    #                 lin = filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value)
    #                 lin += ' ' + str(col3_value)
    #                 print(lin)
    #                 #exec(command)
    #             messages.info(request, str(filename+" processed"))
    #
    #         elif filename == "Scam.csv":
    #             col1_dataframe = csv[[column[0]]]
    #             col2_dataframe = csv[[column[1]]]
    #             col3_dataframe = csv[[column[2]]]
    #
    #             for value in range(csv.shape[0]):
    #                 col1_value = str(col1_dataframe.at[value,column[0]]) # entry_id
    #                 col2_value = str(col2_dataframe.at[value,column[1]]) # reported
    #                 col3_value = str(col3_dataframe.at[value,column[2]]) # scam_type
    #
    #                 entry = Entry.objects.get(entry_id=col1_value)
    #                 rep = BinaryEntry.objects.get(key=col2_value)
    #                 stype = ScamType.objects.get(key=col3_value)
    #
    #                 Scam.objects.create(entry_id=entry,reported=rep,scam_type=stype)
    #                 command=""
    #                 command = "Scam.objects.create(entry_id="
    #                 command += col1_value+",reported="+col2_value+","
    #                 command += "scam_type="+col3_value+")"
    #                 print(command)
    #
    #         elif filename in recurrence_file:
    #             col1_dataframe = csv[[column[0]]]
    #             col2_dataframe = csv[[column[1]]]
    #
    #             for value in range(csv.shape[0]):
    #                 command = ""
    #                 col1_value = int(col1_dataframe.at[value,column[0]]) # entry_id
    #                 col2_value = int(col2_dataframe.at[value,column[1]]) # recurrence
    #                 entry = Entry.objects.get(entry_id=col1_value)
    #                 recurrence = Recurrence.objects.get(key=col2_value)
    #                 if filename.split(".")[0] == "LaptopRecurrence":
    #                     LaptopRecurrence.objects.create(entry_id=entry, key=recurrence)
    #                 elif filename.split(".")[0] == "PCRecurrence":
    #                     PCRecurrence.objects.create(entry_id=entry, key=recurrence)
    #                 elif filename.split(".")[0] == "SmartphoneRecurrence":
    #                     SmartphoneRecurrence.objects.create(entry_id=entry, key=recurrence)
    #                 print(filename.split(".")[0] + " created " + str(col1_value) + " " + str(col2_value) )
    #
    #         elif filename in device_file:
    #             col1_dataframe = csv[[column[0]]]
    #             col2_dataframe = csv[[column[1]]]
    #             col3_dataframe = csv[[column[2]]]
    #             col4_dataframe = csv[[column[3]]]
    #
    #             for value in range(csv.shape[0]):
    #                 #print('\n\n\n test')
    #                 col1_value = str(col1_dataframe.at[value,column[0]]) # entry_id
    #                 col2_value = str(col2_dataframe.at[value,column[1]]) # quantity
    #                 col3_value = str(col3_dataframe.at[value,column[2]]) # utilize
    #                 col4_value = str(col4_dataframe.at[value,column[3]]) # home
    #                 #print('\n\n\n', col1_value)
    #                 # #
    #                 entry = Entry.objects.get(entry_id=col1_value)
    #                 use = BinaryEntry.objects.get(key=col3_value)
    #                 hom = BinaryEntry.objects.get(key=col4_value)
    #
    #                 # if filename.split(".")[0] == "Laptop":
    #                 #     Laptop.objects.create(entry_id=entry, quantity=col2_value, utilize= use, home=hom)
    #                 # elif filename.split(".")[0] == "PC":
    #                 #     PC.objects.create(entry_id=entry, quantity=col2_value, utilize= use, home=hom)
    #                 # elif filename.split(".")[0] == "Smartphone":
    #                 #     Smartphone.objects.create(entry_id=entry, quantity=col2_value, utilize= use, home=hom)
    #                 # if filename.split(".")[0] == "Cellphone":
    #                 # Cellphone.objects.create(entry_id=entry, quantity=col2_value, utilize= use, home=hom)
    #                 # # elif filename.split(".")[0] == "Tablet":
    #                 Tablet.objects.create(entry_id=entry, quantity=col2_value, utilize= use, home=hom)
    #                 # # el
    #                 # # if filename.split(".")[0] == "Smartphone":
    #                 # Smartphone.objects.create(entry_id=entry, quantity=col2_value, utilize= use, home=hom)
    #                 print(filename.split(".")[0] + " created " + col1_value + " " + col2_value + " "+col3_value +" "+ col4_value)
    return render(request, 'home.html')

def results(request):
    print("results")

    donuts = {
        "gender":[{"label":"female", "count":Entry.objects.filter(gender=2).count()},
                  {"label":"male", "count":Entry.objects.filter(gender=1).count()}],
        "age_group":[{"label":"13-17", "count": Entry.objects.filter(age_group=1).count()},
                     {"label":"18-25", "count": Entry.objects.filter(age_group=2).count()},
                     {"label":"26-35", "count": Entry.objects.filter(age_group=3).count()},
                     {"label":"36-45", "count": Entry.objects.filter(age_group=4).count()},
                     {"label":"46-65", "count": Entry.objects.filter(age_group=5).count()}],
        "device": [{"label":"Computer","count":Entry.objects.filter(preferred_device=1).count()},
                   {"label":"Cellphone","count":Entry.objects.filter(preferred_device=2).count()},
                   {"label":"Tablet","count":Entry.objects.filter(preferred_device=3).count()},
                   {"label":"Other","count":Entry.objects.filter(preferred_device=96).count()},
                   {"label":"Not Sure","count":Entry.objects.filter(preferred_device=99).count()}]
    }

    news_source = {
        "printed_media" : {"label":"Printed Media", "count":Entry.objects.filter(news_source=3).count()},
        "social_media" : {"label":"Social Media", "count":Entry.objects.filter(news_source=5).count()},
        "tv" : {"label":"Television", "count":Entry.objects.filter(news_source=1).count()}
        #"" : {"label":, "count":}
    }

    age_min = Entry.objects.all().aggregate(Min('age'))
    age_max = Entry.objects.all().aggregate(Max('age'))

    internet_trust = {
        "trust_level" : {"Very Trustable":1,"Trustable":2,"Little Trust":3,"No Trust":4,"Not Sure":99},
        "age_domain" : [age_min,age_max],
        "trust" : {"Very trustable":"", "count":Entry.objects.filter().count()}
    }



    counts = {
        "printed_media" : {"label":"Printed Media", "count":Entry.objects.filter(news_source=3).count()},
        "scammed" : {"label":"Scammed", "count":Scam.objects.filter().count()},
        "trustable": {"label":"Internet is trustable", "count":Entry.objects.filter(internet_trust=1).count()},
        "millenials":{  "count":Entry.objects.filter(laptop__utilize = 1, age_group = 2).count(),
                        "string":"Millenials use laptops",
                        "total":Entry.objects.filter(age_group=2).count()},
        "baby_boomers":{"label":"Millenials and Laptops",
                        "count":Entry.objects.filter(smartphone__utilize = 1, age_group = 5).count(),
                        "string":"Baby Boomers use smartphones",
                        "total":Entry.objects.filter(age_group=5).count()}
    }

    n = Entry.objects.values('entry_id','age', 'internet_trust','gender')
    nodes = [{
    "key":"female",
    "values":[],
    "color":"#339CFF"},
    {
    "key":"male",
    "values":[],
    "color":"#74DC68"}]
    #print(nodes)
    for item in n:
        if item["gender"] == 1: #
            if item["internet_trust"] == 99:
                nodes[0]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(5-0.3,5+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });
            else:
                nodes[0]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(item["internet_trust"]-0.3,item["internet_trust"]+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });
        else: #male
            if item["internet_trust"] == 99:
                nodes[0]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(5-0.3,5+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });
            else:
                nodes[1]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(item["internet_trust"]-0.3,item["internet_trust"]+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });
    # print(donuts)
    return render(request, 'results.html', {"donuts":donuts, "news_source":news_source, "internet_trust":internet_trust, "counts":counts,"nodes":nodes})


def simple_upload(request):
    return render(request, 'simple_upload.html')


def acknowledgements(request):
    print("ack\n\n\n")

    n = Entry.objects.values('entry_id','age', 'internet_trust','gender')
    nodes = [{
    "key":"female",
    "values":[],
    "color":"#339CFF"},
    {
    "key":"male",
    "values":[],
    "color":"#74DC68"}]
    #print(nodes)
    for item in n:
        if item["gender"] == 1: #
            if item["internet_trust"] == 99:
                nodes[0]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(5-0.3,5+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });
            else:
                nodes[0]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(item["internet_trust"]-0.3,item["internet_trust"]+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });
        else: #male
            if item["internet_trust"] == 99:
                nodes[0]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(5-0.3,5+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });
            else:
                nodes[1]["values"].append({
                    "x":item["age"],
                    "y":round(uniform(item["internet_trust"]-0.3,item["internet_trust"]+0.3), 3),
                    "shape":"circle",
                    "size":round(uniform(0.01,1), 3)
                });


    #values = list(Entry.objects.values_list('age', flat=True))
    #print("nodes", nodes)
    return render(request, 'acknowledgements.html', {"nodes":nodes})
