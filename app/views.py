from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def results(request):
    return render(request, 'results.html')
def simple_upload(request):
    if request.method == 'POST':
        new_types = request.FILES['myfile']
        filename = request.FILES['filename'].name
        print("This is ", filename)
        #django.setup()
        csv = pd.read_csv(request.FILES['myfile'])
        col_names = list(csv.columns.values)

        #the first column name will be for pokemon
        pokemon_model_att = ''
        model_att = ''
        #get the model variables based off of column names
        check_names = (col_names[0], col_names[1])

        column_1_name = col_names[0]
        column_2_name = col_names[1]

        column_1_dataframe = csv[[col_names[0]]]
        print(column_1_dataframe)
        column_2_dataframe = csv[[col_names[1]]]
        #print(poke_num)
        #print(type_num)
        already_checked = []

        if "age_group" in filename:
            for value in range(csv.shape[0]):
                col1_val = int(column_1_dataframe.at[value,col_names[0]])
                col2_val = str(column_2_dataframe.at[value,col_names[1]])
                AgeGroup.objects.get(key= col1_val).type.add(col2_val)
                print('AgeGroup added ' + str(col1_val) + ' ' + str(col2_val))
        elif check_names == ('poke_num', 'level_up_move_num'):
            column_3_dataframe = csv[['level']]
            for value in range(csv.shape[0]):
                col1_val = int(column_1_dataframe.at[value,col_names[0]])
                col2_val = int(column_2_dataframe.at[value,col_names[1]])
                poke = Pokemon.objects.get(number= col1_val)
                move = Moves.objects.get(move_num= col2_val)
                the_level = int(column_3_dataframe.at[value, 'level'])
                LevelUpMove.objects.create(pokemon = poke, move=move, level=the_level)
                print('poke_level_up_move added ' + str(col1_val) + ' ' + str(col2_val))
        elif check_names == ('poke_num', 'egg_move_num'):
            for value in range(csv.shape[0]):
                col1_val = int(column_1_dataframe.at[value,col_names[0]])
                col2_val = str(column_2_dataframe.at[value,col_names[1]])
                Pokemon.objects.get(number= col1_val).egg_moves.add(col2_val)
                print('poke_egg_move added ' + str(col1_val) + ' ' + str(col2_val))
        elif check_names == ('number', 'name'):
            column_3_dataframe = csv[['description']]
            column_4_dataframe = csv[['is_evolved']]
            column_5_dataframe = csv[['male_ratio']]
            column_6_dataframe = csv[['female_ratio']]
            column_7_dataframe = csv[['picture']]
            for value in range(csv.shape[0]):
                col1_val = int(column_1_dataframe.at[value,col_names[0]])
                col2_val = str(column_2_dataframe.at[value,col_names[1]])
                col3_val = str(column_3_dataframe.at[value,'description'])

                val = str(column_4_dataframe.at[value,'is_evolved'])
                col4_val = str_to_bool(val)
                col5_val = str(column_5_dataframe.at[value,'male_ratio'])
                col6_val = str(column_6_dataframe.at[value,'female_ratio'])
                col7_val = str(column_7_dataframe.at[value,'picture'])
                Pokemon.objects.create(number= col1_val, name=col2_val, description=col3_val, is_evolved=col4_val, male_ratio= col5_val, female_ratio=col6_val, picture=col7_val)
                print('pokemon added ' + str(col1_val) + ' ' + str(col2_val))
        else:
            for value in range(csv.shape[0]):
                col1_val = int(column_1_dataframe.at[value,col_names[0]])
                col2_val = str(column_2_dataframe.at[value,col_names[1]])
                Pokemon.objects.get(number= col1_val).egg_groups.add(col2_val)
                print('poke_egg_group_added ' + str(col1_val) + ' ' + str(col2_val))
    return render(request, '../templates/import.html')
