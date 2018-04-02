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
from .models import PC, Laptop, Cellphone, Entry, City
import ast
from django.contrib.auth.models import User
import json
import pandas as pd

# Create your views here.
def home(request):
    print("home")
    # when "upload file" gets clicked
    if request.method == 'POST':
        new_types = request.FILES['myfile']
        # if dict is not empty
        if bool(request.FILES):
            # get filename
            for fn in request.FILES:
                filename = request.FILES[fn].name
                print(filename)

            #use pandas to read csv
            csv = pd.read_csv(request.FILES['myfile'])
            # get list of columns
            column = list(csv.columns.values)

            # the database basically has 5 parts -- 3 groups of similar Tables
            # and 2 unique ones

            two_col_file = ["SocialMedia.csv", "AgeGroup.csv", "Gender.csv",
            "NewsSource.csv", "Device.csv", "TrustLevel.csv", "Department.csv",
            "BinaryEntry.csv", "Recurrence.csv", "ScamType.csv"]
            recurrence_file = ["LaptopRecurrence.csv",
                               "PCRecurrence.csv", "SmartphoneRecurrence.csv"]
            device_file = ["Tablet.csv", "Smartphone.csv", "PC.csv",
                           "Laptop.csv", "Cellphone.csv"]

            if filename in two_col_file:
                col1_dataframe = csv[[column[0]]]
                col2_dataframe = csv[[column[1]]]
                print(column)
                for value in range(csv.shape[0]): # no. of rows to be read
                    command = ""
                    col1_value = int(col1_dataframe.at[value,column[0]])
                    col2_value = str(col2_dataframe.at[value,column[1]])
                    command = filename.split(".")[0]+".objects.create("+column[0]+"="
                    command += str(col1_value)+", "+column[1]+"=\'"+str(col2_value)+"\')"
                    print(command)
                    exec(command)
                messages.info(request, str(filename+" processed"))

            elif filename == "Entry.csv":
                col1_dataframe = csv[[column[0]]]
                col2_dataframe = csv[[column[1]]]
                col3_dataframe = csv[[column[2]]]
                col4_dataframe = csv[[column[3]]]
                col5_dataframe = csv[[column[4]]]
                col6_dataframe = csv[[column[5]]]
                col7_dataframe = csv[[column[6]]]
                col8_dataframe = csv[[column[7]]]
                col9_dataframe = csv[[column[8]]]

                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = str(col1_dataframe.at[value,column[0]]) # entry_id
                    col2_value = str(col2_dataframe.at[value,column[1]]) # household_size
                    col3_value = str(col3_dataframe.at[value,column[2]]) # age
                    col4_value = str(col4_dataframe.at[value,column[3]]) # city
                    col5_value = str(col5_dataframe.at[value,column[4]]) # social_media
                    col6_value = str(col6_dataframe.at[value,column[5]]) # news_source
                    col7_value = str(col7_dataframe.at[value,column[6]]) # internet_trust
                    col8_value = str(col8_dataframe.at[value,column[7]]) # preferred_device
                    col9_value = str(col9_dataframe.at[value,column[8]]) # gender
                    Entry.objects.create(entry_id=col1_value,
                                         household_size=col2_value,
                                         age=col3_value,
                                         city=City.objects.get(key=col4_value),
                                         social_media=SocialMedia.objects.get(key=col5_value),
                                         news_source=NewsSource.objects.get(key=col6_value),
                                         internet_trust=TrustLevel.objects.get(key=col7_value),
                                         preferred_device=Device.objects.get(key=col8_value),
                                         gender=Gender.objects.get(key=col9_value))
                    # command = filename.split(".")[0]+".objects.create("+column[0]+"="
                    # command += col1_value+","+column[1]+"="+col2_value
                    # command += ","+column[2]+"="+col3_value+","+column[3]+"=\'"+col4_value+"\',"+column[4]+"=\'"
                    # command += col5_value+"\',"+column[5]+"=\'"+col6_value+"\',"+column[6]+"=\'"
                    # command += col7_value+"\',"+column[7]+"=\'"+col8_value
                    # command += "\',"+column[8]+"=\'"+col9_value+"\')"
                    #
                    # print(command)
                    print('\n\n\n', column)
                    #exec(command)
                messages.info(request, str(filename+" processed"))
                    # AgeGroup.objects.get(key=col1_value).type.add(col2_value)
                    # print(filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value))

            elif filename == "City.csv":
                col1_dataframe = csv[[column[0]]]
                col2_dataframe = csv[[column[1]]]
                col3_dataframe = csv[[column[2]]]

                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = str(col1_dataframe.at[value,column[0]]) # key
                    col2_value = str(col2_dataframe.at[value,column[1]]) # name
                    col3_value = str(col3_dataframe.at[value,column[2]]) # department
                    dept = Department.objects.get(key=col3_value)

                    City.objects.create(key=col1_value,name=col2_value,department=dept)
                    print(command)
                    #exec(command)
                messages.info(request, str(filename+" processed"))

            elif filename == "Scam.csv":
                col1_dataframe = csv[[column[0]]]
                col2_dataframe = csv[[column[1]]]
                col3_dataframe = csv[[column[2]]]

                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = str(col1_dataframe.at[value,column[0]]) # entry_id
                    col2_value = str(col2_dataframe.at[value,column[1]]) # reported
                    col3_value = str(col3_dataframe.at[value,column[2]]) # scam_type
                    command = filename.split(".")[0] + ".objects.create(entry_id="
                    command += col1_value+",reported="+col2_value+","
                    command += "scam_type="+col3_value+")"
                    print("\n\n\n\n\n")

                    print(command)
                    exec(command)
                messages.info(request, str(filename+" processed"))

            elif filename in recurrence_file:
                col1_dataframe = csv[[column[0]]]
                col2_dataframe = csv[[column[1]]]

                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = int(col1_dataframe.at[value,column[0]])
                    col2_value = int(col2_dataframe.at[value,column[1]])
                    # build command
                    command = filename.split(".")[0] + ".objects.create("+column[0]+"="
                    command += str(col1_value)+","+column[1]+"="+str(col2_value)+")"
                    print(command)
                    exec(command)
                print(col_names) # key, gender

            elif filename in device_file:
                col1_dataframe = csv[[column[0]]]
                col2_dataframe = csv[[column[1]]]
                col3_dataframe = csv[[column[2]]]
                col4_dataframe = csv[[column[3]]]

                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = int(col1_dataframe.at[value,column[0]]) # entry_id
                    col2_value = int(col2_dataframe.at[value,column[1]]) # quantity
                    col3_value = int(col2_dataframe.at[value,column[2]]) # utilize
                    col4_value = int(col2_dataframe.at[value,column[3]]) # home
                    command = filename.split(".")[0] + ".objects.create("+column[0]+"="
                    command += col1_value+","+column[1]+" ="+col2_value+","+column[2]+"="+col3_value
                    command += ","+column[3]+"="+col4_value+")"
                    print(command)
                    exec(command)
                print(col_names) # key, gender
                messages.info(request, str(filename+" processed"))
    return render(request, 'home.html')

def results(request):
    return render(request, 'results.html')
def simple_upload(request):
    print("import\n\n\n")
    return render(request, 'simple_upload.html')
def three(request):
    print("three\n\n\n")
    return render(request, 'three.html')
