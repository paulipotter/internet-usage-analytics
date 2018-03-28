from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django import forms
from .models import AgeGroup
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

            two_col_file = ["SocialMedia.csv", "AgeGroup.csv", "Gender.csv",
            "NewsSource.csv", "Devices.csv", "TrustLevel.csv", "Department.csv",
            "BinaryEntry.csv", "Recurrence.csv", "ScamType.csv"]

            recurrence_file = ["LaptopRecurrence.csv",
                               "PCRecurrence.csv", "SmartphoneRecurrence.csv"]

            device_file = ["Tablets.csv", "Smartphones.csv", "PCs.csv",
                           "Laptops.csv", "Cellphones.csv"]

            if filename in two_col_file:
                print(column)
                command = ""
                for value in range(csv.shape[0]): # no. of rows to be read
                    col1_value = int(col1_dataframe.at[value,column[0]])
                    col2_value = str(col2_dataframe.at[value,column[1]])
                    command=filename.split(".")[0]+".objects.create(key=col1_value).type.add(col2_value)""
                    print(filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value))

            elif filename == "Entry.csv":
                for value in range(csv.shape[0]):
                    col1_value = int(col1_dataframe.at[value,column[0]]) # entry_id
                    col2_value = int(col2_dataframe.at[value,column[1]]) # household_size
                    col3_value = int(col2_dataframe.at[value,column[2]]) # age
                    col4_value = str(col2_dataframe.at[value,column[3]]) # city
                    col5_value = str(col2_dataframe.at[value,column[4]]) # social_media
                    col6_value = str(col2_dataframe.at[value,column[5]]) # news_source
                    col7_value = str(col2_dataframe.at[value,column[6]]) # internet_trust
                    col8_value = str(col2_dataframe.at[value,column[7]]) # preferred_device
                    col9_value = str(col2_dataframe.at[value,column[8]]) # gender
                    # AgeGroup.objects.get(key=col1_value).type.add(col2_value)
                    print(filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value))

            elif filename == "city.csv":
                for value in range(csv.shape[0]):
                    col1_value = int(col1_dataframe.at[value,column[0]]) # key
                    col2_value = str(col2_dataframe.at[value,column[1]]) # name
                    col3_value = int(col2_dataframe.at[value,column[2]]) # department

            elif filename in recurrence_file:
                for value in range(csv.shape[0]):
                    col1_value = int(col1_dataframe.at[value,column[0]])
                    col2_value = int(col2_dataframe.at[value,column[1]])
                print(col_names) # key, gender

            elif filename in device_file:
                command = ""
                for value in range(csv.shape[0]):
                    col1_value = int(col1_dataframe.at[value,column[0]]) # entry_id
                    col2_value = int(col2_dataframe.at[value,column[1]]) # quantity
                    col3_value = int(col2_dataframe.at[value,column[2]]) # utilize
                    col4_value = int(col2_dataframe.at[value,column[3]]) # home
                command = filename.split(".")[0] + "objects.create( entry_id="
                command += col1_val+",quantity ="+col2_value+",utilize="+col3_value
                command += ",home="+col4_value+")"  
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
