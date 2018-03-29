from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django import forms
from .models import AgeGroup, SocialMedia, Gender, NewsSource, Device, TrustLevel
from .models import Department, BinaryEntry, Recurrence, ScamType, LaptopRecurrence
from .models import PCRecurrence, SmartphoneRecurrence, Tablet, Smartphone
from .models import PC, Laptop, Cellphone, Entry, City
import ast
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
            col1_dataframe = csv[[column[0]]]
            col2_dataframe = csv[[column[1]]]

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
                print(column)
                command = ""
                for value in range(csv.shape[0]): # no. of rows to be read
                    col1_value = int(col1_dataframe.at[value,column[0]])
                    col2_value = str(col2_dataframe.at[value,column[1]])
                    command = filename.split(".")[0]+".objects.create(key="
                    command += col1_value+", name="+col2_value+")"

                    # print(filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value))

            elif filename == "Entry.csv":
                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = int(col1_dataframe.at[value,column[0]]) # entry_id
                    col2_value = int(col2_dataframe.at[value,column[1]]) # household_size
                    col3_value = int(col2_dataframe.at[value,column[2]]) # age
                    col4_value = str(col2_dataframe.at[value,column[3]]) # city
                    col5_value = str(col2_dataframe.at[value,column[4]]) # social_media
                    col6_value = str(col2_dataframe.at[value,column[5]]) # news_source
                    col7_value = str(col2_dataframe.at[value,column[6]]) # internet_trust
                    col8_value = str(col2_dataframe.at[value,column[7]]) # preferred_device
                    col9_value = str(col2_dataframe.at[value,column[8]]) # gender
                    command = filename.split(".")[0]+".objects.create(entry_id="
                    command += col1_value+",household_size="+col2col2_value
                    command += ",age="+col3_value+",city="+col4_value+",social_media="
                    command += col5_value+",news_source="+col6_value+",internet_trust="
                    command += col7_value+",preferred_device="+col8_value
                    command += ",gender"+col9_value+")"
                    print(command)
                    exec(command)
                    # AgeGroup.objects.get(key=col1_value).type.add(col2_value)
                    # print(filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value))

            elif filename == "City.csv":
                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = int(col1_dataframe.at[value,column[0]]) # key
                    col2_value = str(col2_dataframe.at[value,column[1]]) # name
                    col3_value = int(col2_dataframe.at[value,column[2]]) # department
                    command = filename.split(".")[0] + ".objects.create(key="
                    command = col1_value+",name="+col2_value+",department="+col3_value
                    print(command)
                    exec(command)

            elif filename in recurrence_file:
                for value in range(csv.shape[0]):
                    col1_value = int(col1_dataframe.at[value,column[0]])
                    col2_value = int(col2_dataframe.at[value,column[1]])
                    # #build command
                    command = filename.split(".")[0] + ".objects.create(entry_id="
                    command += col1_value+",key ="+col2_value+")"
                    print(command)
                    exec(command)
                print(col_names) # key, gender

            elif filename in device_file:
                for value in range(csv.shape[0]):
                    command = ""
                    col1_value = int(col1_dataframe.at[value,column[0]]) # entry_id
                    col2_value = int(col2_dataframe.at[value,column[1]]) # quantity
                    col3_value = int(col2_dataframe.at[value,column[2]]) # utilize
                    col4_value = int(col2_dataframe.at[value,column[3]]) # home
                    command = filename.split(".")[0] + ".objects.create(entry_id="
                    command += col1_value+",quantity ="+col2_value+",utilize="+col3_value
                    command += ",home="+col4_value+")"
                    print(command)
                    exec(command)
                print(col_names) # key, gender

    return render(request, 'home.html')

def results(request):
    return render(request, 'results.html')
def simple_upload(request):
    print("import\n\n\n")
    return render(request, 'simple_upload.html')
def three(request):
    print("three\n\n\n")
    return render(request, 'three.html')
