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

            two_col_file = ["social_media.csv", "age_group.csv", "gender.csv",
            "news_source.csv", "devices.csv", "trust_level.csv", "departments.csv",
            "binary_entry.csv", "recurrence.csv", "scam_type.csv"]

            recurrence_file = ["laptop_recurrence.csv",
                               "pc_recurrence.csv", "smartphone_recurrence.csv"]

            device_file = ["tablets.csv", "smartphones.csv", "pcs.csv",
                           "laptops.csv", "cellphones.csv"]

            if filename in two_col_file:
                print(column)
                for value in range(csv.shape[0]): # no. of rows to be read
                    col1_value = int(col1_dataframe.at[value,column[0]])
                    col2_value = str(col2_dataframe.at[value,column[1]])
                    # AgeGroup.objects.get(key=col1_value).type.add(col2_value)
                    print(filename.split(".")[0]+' added ' + str(col1_value) + ' ' + str(col2_value))

            elif filename == "entries.csv":
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


    return render(request, 'home.html')

def results(request):
    return render(request, 'results.html')
def simple_upload(request):
    print("import\n\n\n")
    return render(request, 'simple_upload.html')
def three(request):
    print("three\n\n\n")
    return render(request, 'three.html')
