from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django import forms
import ast
import json
import pandas as pd

# Create your views here.
def home(request):
    print("home")
    if request.method == 'POST':
        new_types = request.FILES['myfile']
        # get filename
        if bool(request.FILES):
            for fn in request.FILES:
                filename = request.FILES[fn].name
                print(filename)
            csv = pd.read_csv(request.FILES['myfile'])
            col_names = list(csv.columns.values)
            print(col_names)
            if filename == "age_group.csv":
                for value in range(csv.shape[0]):
                    col1_val = int(column_1_dataframe.at[value,col_names[0]])
                    col2_val = str(column_2_dataframe.at[value,col_names[1]])
                    AgeGroup.objects.get(key= col1_val).type.add(col2_val)
                    print('AgeGroup added ' + str(col1_val) + ' ' + str(col2_val))

    return render(request, 'home.html')

def results(request):
    return render(request, 'results.html')
def simple_upload(request):
    print("import\n\n\n")
    return render(request, 'simple_upload.html')
def three(request):
    print("three\n\n\n")
    return render(request, 'three.html')
