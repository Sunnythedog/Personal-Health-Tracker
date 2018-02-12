# health.py started 12/31/17 @ 12:40 pm revision 0.1
# Created to track my health

import sqlite3
import time
import csv

conn = sqlite3.connect('health.db')
c = conn.cursor()

# Blood Pressure menu selection for database input

def blood_pressure():

    def blood_pressure_menu():
        print('1 - Add Data to Database')
        print('2 - View Inputted Data')
        print('3 - Return to Main Menu')
        print("")
        selection = input('Enter Selection: ')
        print("")

        if selection == '1':
            create_table_blood_pressure()
            blood_pressure_dynamic_data_entry()
        elif selection == '2':
            create_table_blood_pressure()
            read_from_db_blood_pressure()
        elif selection == '3':
            main_menu()
        else:
            print('Unknown option selected, please choose again')
            blood_pressure_menu()

    def create_table_blood_pressure():
        c.execute('CREATE TABLE IF NOT EXISTS blood_pressure(unix REAL, systolic INT, diastolic INT, heart_rate INT)')

    def blood_pressure_dynamic_data_entry():
        unix = time.time()
        systolic = input('enter systolic rate: ')
        diastolic = input('enter diastolic rate: ')
        heart_rate = input('enter heart rate: ')
        c.execute("INSERT INTO blood_pressure (unix, systolic, diastolic, heart_rate) VALUES (?, ?, ?, ?)",
                  (unix, systolic, diastolic, heart_rate))
        conn.commit()

    def read_from_db_blood_pressure():
        c.execute('SELECT * FROM blood_pressure')
        for row in c.fetchall():
            print(row)

    blood_pressure_menu()

    main_menu()

# Blood Test menu selection for database input (33 Values)

def blood_test():

    def create_table_blood_test():
        c.execute("""CREATE TABLE IF NOT EXISTS blood_test(date TEXT, WBC REAL, RBC REAL, 
        HGB REAL, HCT REAL, MCV REAL, MCH REAL, MCH_C REAL, RDW REAL, PLT REAL, MPV REAL, 
        Glu REAL, BUN REAL, BUNCreat REAL, Calcium REAL, Na REAL, K REAL, Cl REAL, CO2 REAL, 
        TP REAL, Alb REAL, AG REAL, Tbili REAL, AlkPhos REAL, AST REAL, ALT REAL, Anion REAL, 
        GFR REAL, Chol REAL, Trig REAL, HDL REAL, LDL REAL, VLDL REAL)""")

    def blood_test_dynamic_data_entry():
        print('')
        date = input('Enter date of blood test: ')
        WBC = input('Enter WBC (White Blood Cell): ')
        RBC = input('Enter RBC (Red Blood Cell): ')
        HGB = input('Enter HGB (): ')
        HCT = input('Enter HCT (Hematocrit): ')
        MCV = input('Enter MCV (): ')
        MCH = input('Enter MCH (): ')
        MCH_C = input('Enter MCHC (): ')
        RDW = input('Enter RDW (): ')
        PLT = input('Enter PLT (): ')
        MPV = input('Enter MPV (): ')
        Glu = input('Enter Glu (): ')
        BUN = input('Enter BUN (Blood Urea Nitrogen (kidney function test)): ')
        BUNCreat = input('Enter BUNCreat (): ')
        Calcium = input('Enter Calcium: ')
        Na = input('Enter sodium: ')
        K = input('Enter K (Potassium): ')
        Cl = input('Enter Cl ()')
        CO2 = input('Enter CO2: ')
        TP = input('Enter TP (): ')
        Alb = input('Enter Alb (): ')
        AG = input('Enter AG (): ')
        Tbili = input('Enter Tbili (): ')
        AlkPhos = input('Enter AlkPhos (): ')
        AST = input('Enter AST (): ')
        ALT = input('Enter ALT (): ')
        Anion = input('Enter Anion (): ')
        GFR = input('Enter GFR (): ')
        Chol = input('Enter Chol (Cholesterol): ')
        Trig = input('Enter Trig (Triglycerides): ')
        HDL = input('Enter HDL: ')
        LDL = input('Enter LDL: ')
        VLDL = input('Enter VLDL: ')
        c.execute("""INSERT INTO blood_test(date, WBC, RBC, HGB, HCT, 
        MCV, MCH, MCH_C, RDW, PLT, MPV, Glu, BUN, BUNCreat,Calcium, 
        Na, K, Cl, CO2, TP, Alb, AG, Tbili, AlkPhos, AST, ALT, Anion, 
        GFR, Chol, Trig, HDL, LDL, VLDL) 
        VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)""",
        (date, WBC, RBC, HGB, HCT, MCV, MCH, MCH_C, RDW, PLT, MPV, Glu, BUN, BUNCreat, Calcium, Na, K, Cl, CO2, TP, Alb,
         AG, Tbili, AlkPhos, AST, ALT, Anion, GFR, Chol, Trig, HDL, LDL, VLDL))
        conn.commit()

    def read_from_db_blood_test():
        c.execute('SELECT * FROM blood_test')
        for row in c.fetchall():
            print(row)

    create_table_blood_test()
    blood_test_dynamic_data_entry()
    read_from_db_blood_test()

    main_menu()

# Body temperature upload/download to database

def body_temperature():

    def create_table_body_temperature():
        c.execute('CREATE TABLE IF NOT EXISTS body_temperature(unix REAL, temperature REAL, feeling TEXT)')

    def body_temperature_dynamic_data_entry():
        unix = time.time()
        temperature = input('Enter Body Temperature: ')
        feeling = input('Enter how you are feeling today: ')
        c.execute("INSERT INTO body_temperature(unix, temperature, feeling) VALUES (?, ?, ?)",
                  (unix, temperature, feeling))
        conn.commit()

    def read_from_db_body_temperature():
        c.execute('SELECT * FROM body_temperature')
        for row in c.fetchall():
            print(row)

    create_table_body_temperature()
    body_temperature_dynamic_data_entry()
    read_from_db_body_temperature()

    main_menu()


# Nutritional Information and daily food tracker
def diet():

    def nutritional_data_table():
        c.execute('''CREATE TABLE IF NOT EXISTS nutritional_data(food TEXT, serving_size REAL, serving_unit_size TEXT, food_group TEXT,
        calories INT, saturated_fat REAL, trans_fat REAL, monounsaturated_fatty_acid REAL, polyunsaturated_fatty_acids REAL, cholesterol REAL, sodium REAL, fiber REAL, 
        total_sugars REAL, protein REAL, chromium REAL, copper REAL, flouride REAL, iodine REAL, iron REAL, manganese REAL, antioxidents REAL,
        molybdenum REAL, selenium REAL, zinc REAL, calcium REAL, chloride REAL, magnesium REAL, phosphorus REAL,
        potassium REAL, sulfur REAL, vitamin_a REAL, vitamin_c REAL, vitamin_d REAL, vitamin_e REAL, vitamin_k REAL, biotin_b7 REAL, 
        folic_acid_b9 REAL, niacin_b3 REAL, pantothenic_acid_b5 REAL, riboflavin_b2 REAL, thiamin_b1 REAL, vitamin_b6 REAL, vitamin_b12 REAL, betaine REAL,
        choline REAL, folate REAL, ash REAL, alanine REAL, histidine REAL, proline REAL, arginine REAL, isoleucine REAL, serine REAL, aspartic_acid REAL, 
        leucine REAL, threonine REAL, cystine REAL, lysine REAL, tyrosine REAL, glutamic_acid REAL, methionine REAL, valine REAL, glycine_REAL, phenylalanine REAL,
        omega_3 REAL, omega_6 REAL, phytosterols REAL, alcohol REAL, water REAL, caffeine REAL, theobromine REAL, trans_monoenoic_fatty_acids REAL, 
        trans_polyenoic_fatty_acid REAL)''')

        print('')
        food = input('Enter food: ')
        serving_size = input('Enter serving size: ')
        serving_unit_size = input("Enter units of serving (cups, grams, etc): ")
        food_group = input("Enter food group (Bread, Cereal, Rice & Pasta (6-11), Vegetable Group (3-5), Fruit Group (2-4), Meat, Poultry, Dry Beans, eggs (2-3), Milk, yougurt, cheese (), Fats, Oils, & sweets (Use Saparingly): ")
        calories = input('Enter calories: ')
        saturated_fat = input('Enter saturated fat: ')
        trans_fat = input('Enter Trans Fat: ')
        monounsaturated_fatty_acid = input("Enter monosaturated fatty acid: ")
        polyunsaturated_fatty_acids = input("Enter polyunsaturated fatty acids: ")
        cholesterol = input("Enter cholesterol: ")
        sodium = input("Enter sodium: ")
        fiber = input("Enter fiber: ")
        total_sugars = input("Enter total sugars: ")
        protein = input("Enter protein: ")
        chromium = input("Enter chromium: ")
        copper = input("Enter copper: ")
        flouride = input("Enter flouride: ")
        iodine = input('Enter iodine: ')
        iron = input('Enter iron: ')
        maganese = input('Enter maganese: ')
        antioxidents = input("Enter Antiocidents: ")
        molybdeum = input("Enter molybdeum: ")
        selenium = input('Enter selenium: ')
        zinc = input('Enter zinc: ')
        calcium = input('Enter calcium: ')
        chloride = input('Enter chloride: ')
        magnesium = input('Enter magnesium: ')
        phosphorus = input('Enter phosphorus: ')
        potassium = input("Enter potassium: ")
        sulfur = input("Enter sulfur: ")
        vitamin_a = input('Enter Vitamin A: ')
        vitamin_c = input('Enter Vitamin C: ')
        vitamin_d = input('Enter Vitamin D: ')
        vitamin_e = input('Enter Vitamin E: ')
        vitamin_k = input('Enter Vitamin K: ')
        biotin_b7 = input('Enter Vitamin B7: ')
        folic_acid_b9 = input("Enter folic acid: ")
        niacin_b3 = input("Enter Niacin B3: ")
        pantothenic_acid_b5 = input("Enter Pantothenic Acid B5: ")
        riboflavin_b2 = input('Enter Riboflavin B2: ')
        thiamin_b1 = input('Enter Thiamin B1: ')
        vitamin_b6 = input('Enter Vitamin B6: ')
        vitamin_b12 = input("Enter Vitamin B12: ")
        betaine = input('Enter Betaine: ')
        choline = input('Enter Choline: ')
        folate = input('Enter folate: ')
        ash = input("Enter Ash: ")
        alanine = input('Enter Alanine: ')
        histidine = input('Enter Histidine: ')
        proline = input('Enter Proline: ')
        arginine = input('Enter Arginine: ')
        isoleucine = input('Enter Isoleucine: ')
        serine = input('Enter Serine: ')
        aspartic_acid = input("Enter Aspartic Acid: ")
        leucine = input('Enter Leucine: ')
        threonine = input('Enter Threonine: ')
        cystine = input('Enter Cystine: ')
        lysine = input('Enter Lysine: ')
        tyrosine = input('Enter tyrosine: ')
        glutamic_acid = input('Enter Glutamic Acid: ')
        methionine = input('Enter Methionine: ')
        valine = input("Enter valine: ")
        glycine = input("Enter glycine: ")
        phenylalanine = input('Enter Phenylalanine: ')
        omega_3 = input("Enter Omega 3: ")
        omega_6 = input("Enter Omega 6: ")
        phytosterols = input("Enter Phytosterols: ")
        alcohol = input("Enter Alcohol: ")
        water = input("Enter Water: ")
        caffeine = input("Enter caffeine: ")
        theobromine = input("Enter Theobromine: ")
        trans_monoenoic_fatty_acids = input("Enter Trans Monoenoic Fatty Acids: ")
        trans_polyenoic_fatty_acid = input("Enter Polyenoic Fatty Acid: ")

        c.execute("""INSERT INTO nutritional_data(food, serving_size, serving_unit_size, food_group, calories, saturated_fat, trans_fat, 
        monounsaturated_fatty_acid, polyunsaturated_fatty_acids, cholesterol, sodium, fiber, total_sugars, protein, chromium, copper,
        flouride, iodine, iron, maganese, antioxidents, molybdeum, selenium, zinc, calcium, chloride, magnesium, phosphorus,
        potassium, sulfur, vitamin_a, vitamin_c, vitamin_d, vitamin_e, vitamin_k, biotin_b7, 
        folic_acid_b9, niacin_b3, pantothenic_acid_b5, riboflavin_b2, thiamin_b1, vitamin_b6, vitamin_b12, betaine,
        choline, folate, ash, alanine, histidine, proline, arginine, isoleucine, serine, aspartic_acid, 
        leucine, threonine, cystine, lysine, tyrosine, glutamic_acid, methionine, valine, glycine, phenylalanine,
        omega_3, omega_6, phytosterols, alcohol, water, caffeine, theobromine, trans_monoenoic_fatty_acids, 
        trans_polyenoic_fatty_acid) 
        VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (food, serving_size, serving_unit_size, food_group, calories, saturated_fat, trans_fat, monounsaturated_fatty_acid,
        polyunsaturated_fatty_acids, cholesterol, sodium, fiber, total_sugars, protein, chromium, copper,
        flouride, iodine, iron, maganese, antioxidents, molybdeum, selenium, zinc, calcium, chloride, magnesium, phosphorus,
        potassium, sulfur, vitamin_a, vitamin_c, vitamin_d, vitamin_e, vitamin_k, biotin_b7,
        folic_acid_b9, niacin_b3, pantothenic_acid_b5, riboflavin_b2, thiamin_b1, vitamin_b6, vitamin_b12, betaine,
        choline, folate, ash, alanine, histidine, proline, arginine, isoleucine, serine, aspartic_acid,
        leucine, threonine, cystine, lysine, tyrosine, glutamic_acid, methionine, valine, glycine, phenylalanine,
        omega_3, omega_6, phytosterols, alcohol, water, caffeine, theobromine, trans_monoenoic_fatty_acids,
        trans_polyenoic_fatty_acid))
        conn.commit()

    def daily_food_tracker_table():
        c.execute('CREATE TABLE IF NOT EXISTS daily_food_tracker(date TEXT)')

    def diet_menu():
        print('')
        print('1 - Daily food tracker')
        print('2 - input new food nutritional data')
        print('')
        selection = input('Please enter a selection m to return to main menu: ')
        print('')

        if selection == '1':
            daily_food_tracker_table()
        elif selection == '2':
            nutritional_data_table()
        elif selection == 'm':
            main_menu()
        else:
            print ('Unknown option selected, please choose again')
            diet_menu()
            print('')

    diet_menu()

# Upload Apple Health csv data to database

def upload_apple_data():

        c.execute('''CREATE TABLE IF NOT EXISTS apple_health_data(Start TEXT,Finish TEXT,Active Calories (kcal) REAL,
        Biotin (mcg) REAL,Blood Alcohol Content (%) REAL,Blood Glucose (mg/dL) REAL,Blood Pressure (Diastolic) (mmHg) REAL,
        Blood Pressure (Systolic) (mmHg) REAL,Body Fat Percentage (%) REAL,Body Mass Index (count) REAL,Body Temperature (degC) REAL,
        Basal Body Temperature (degC) REAL,Caffeine (mg) REAL,Calcium (mg) REAL,Carbohydrates (mg) REAL,Chloride (mg) REAL,
        Cholesterol (mg) REAL,Chromium (mcg) REAL,Copper (mcg) REAL,Cycling Distance (mi) REAL,Dietary Calories (cal) REAL,Distance (mi) REAL,
        Electrodermal Activity (mcS) REAL,Fiber (g) REAL,Flights Climbed (count) REAL,Folate (mcg) REAL,Forced Expiratory Volume (L) REAL,
        Forced Vital Capacity (L) REAL,Heart Rate (count/min) REAL,Inhaler Usage (count) REAL,Iodine (mcg) REAL,Lean Body Mass (lb) REAL,
        Magnesium (mg) REAL,Manganese (mg) REAL,Molybdenum (mcg) REAL,Monosaturated Fat (g) REAL,Niacin (mg) REAL,NikeFuel (count) REAL,
        Number of Times Fallen (count) REAL,Oxygen Saturation (%) REAL,Pantothenic Acid (mg) REAL,Peak Expiratory Flow Rate (L/min) REAL,
        Peripheral Perfusion Index (%) REAL,Phosphorus (mg) REAL,Polyunsaturated Fat (g) REAL,Potassium (mg) REAL,Protein (g) REAL,
        Respiratory Rate (count/min) REAL,Resting Calories (kcal) REAL,Riboflavin (mg) REAL,Saturated Fat (g) REAL,Selenium (mcg) REAL,
        Sodium (mg) REAL,Steps (count) REAL,Sugar (g) REAL,Thiamin (mg) REAL,Total Fat (g) REAL,Vitamin A (mcg) REAL,Vitamin B12 (mcg) REAL,
        Vitamin B6 (mg) REAL,Vitamin C (mg) REAL,Vitamin D (mcg) REAL,Vitamin E (mg) REAL,Vitamin K (mcg) REAL,Weight (lb) REAL,
        Dietary Water (L) REAL,Zinc (mg) REAL,UV Exposure (count) REAL)''')

        with open('Health Data.csv', 'rb') as fin:
            dr = csv.DictReader(fin)
            to_db = []
            for i in dr:
                to_db.append((i['Start'], i['Finish'], i['Active Calories (kcal)'], i['Biotin (mcg)'],
                              i['Blood Alcohol Content (%)'],
                              i['Blood Glucose (mg/dL)'], i['Blood Pressure (Diastolic) (mmHg)'],
                              i['Blood Pressure (Systolic) (mmHg)'],
                              i['Body Fat Percentage (%)'], i['Body Mass Index (count)'], i['Body Temperature (degC)'],
                              i['Basal Body Temperature (degC)'],
                              i['Caffeine (mg)'], i['Calcium (mg)'], i['Carbohydrates (mg)'], i['Chloride (mg)'],
                              i['Cholesterol (mg)'],
                              i['Chromium (mcg)'], i['Copper (mcg)'], i['Cycling Distance (mi)'],
                              i['Dietary Calories (cal)'],
                              i['Distance (mi)'], i['Electrodermal Activity (mcS)'], i['Fiber (g)'],
                              i['Flights Climbed (count)'],
                              i['Folate (mcg)'], i['Forced Expiratory Volume (L)'], i['Forced Vital Capacity (L)'],
                              i['Heart Rate (count/min)'],
                              i['Inhaler Usage (count)'], i['Iodine (mcg)'], i['Lean Body Mass (lb)'],
                              i['Magnesium (mg)'], i['Manganese (mg)'],
                              i['Molybdenum (mcg)'], i['Monosaturated Fat (g)'], i['Niacin (mg)'],
                              i['NikeFuel (count)'], i['Number of Times Fallen (count)'],
                              i['Oxygen Saturation (%)'], i['Pantothenic Acid (mg)'],
                              i['Peak Expiratory Flow Rate (L/min)'], i['Peripheral Perfusion Index (%)'],
                              i['Phosphorus (mg)'], i['Polyunsaturated Fat (g)'], i['Potassium (mg)'], i['Protein (g)'],
                              i['Respiratory Rate (count/min)'],
                              i['Resting Calories (kcal)'], i['Riboflavin (mg)'], i['Saturated Fat (g)'], i['Selenium (mcg)'],
                              i['Sodium (mg)'],
                              i['Steps (count)'], i['Sugar (g)'], i['Thiamin (mg)'], i['Total Fat (g)'], i['Vitamin A (mcg)'],
                              i['Vitamin B12 (mcg)'],
                              i['Vitamin B6 (mg)'], i['Vitamin C (mg)'], i['Vitamin D (mcg)'], i['Vitamin E (mg)'],
                              i['Vitamin K (mcg)'], i['Weight (lb)'],
                              i['Dietary Water (L)'], i['Zinc (mg)'], i['UV Exposure (count)']))

            c.execute('''INSERT INTO apple_health_data(Start,Finish,Active Calories (kcal),Biotin (mcg),Blood Alcohol Content (%),
                          Blood Glucose (mg/dL),Blood Pressure (Diastolic) (mmHg),Blood Pressure (Systolic) (mmHg),
                          Body Fat Percentage (%),Body Mass Index (count),Body Temperature (degC),Basal Body Temperature (degC),
                          Caffeine (mg),Calcium (mg),Carbohydrates (mg),Chloride (mg),Cholesterol (mg),Chromium (mcg),
                          Copper (mcg),Cycling Distance (mi),Dietary Calories (cal),Distance (mi),Electrodermal Activity (mcS),
                          Fiber (g),Flights Climbed (count),Folate (mcg),Forced Expiratory Volume (L),
                          Forced Vital Capacity (L),Heart Rate (count/min),Inhaler Usage (count),Iodine (mcg),Lean Body Mass (lb),
                          Magnesium (mg),Manganese (mg),Molybdenum (mcg),Monosaturated Fat (g),Niacin (mg),NikeFuel (count),
                          Number of Times Fallen (count),Oxygen Saturation (%),Pantothenic Acid (mg),Peak Expiratory Flow Rate (L/min),
                          Peripheral Perfusion Index (%),Phosphorus (mg),Polyunsaturated Fat (g),Potassium (mg),Protein (g),
                          Respiratory Rate (count/min),Resting Calories (kcal),Riboflavin (mg),Saturated Fat (g),Selenium (mcg),
                          Sodium (mg),Steps (count),Sugar (g),Thiamin (mg),Total Fat (g),Vitamin A (mcg),Vitamin B12 (mcg),
                          Vitamin B6 (mg),Vitamin C (mg),Vitamin D (mcg),Vitamin E (mg),Vitamin K (mcg),Weight (lb),
                          Dietary Water (L),Zinc (mg),UV Exposure (count)) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                          ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', (to_db))

            conn.commit()

# Main Menu

def main_menu():

    print('')
    print('1 - Blood Pressure')
    print('2 - Blood Test Results')
    print('3 - Weight, PWV, Bone Weight, Muscle Weight, Body Fat Percentage, Water')
    print('4 - Body Temperature')
    print('5 - Diet')
    print('6 - Exercise')
    print('7 - O2 Levels')
    print('8 - Upload Apple Health Data')
    print('q - To Quit')
    print('')

    menu_selection = input('Make a selection: ')
    print('')

    if menu_selection == '1':
        blood_pressure()
    elif menu_selection == '2':
        blood_test()
    elif menu_selection == '3':
        print('three')
    elif menu_selection == '4':
        body_temperature()
    elif menu_selection == '5':
        diet()
    elif menu_selection == '6':
        print ('six')
    elif menu_selection == '7':
        print ('seven')
    elif menu_selection == '8':
        upload_apple_data()
    elif menu_selection == 'q':
        print('quit')
    else:
        print ('Unknown option selected, please choose again')
        main_menu()
        print('')

# Main program

main_menu()

c.close()
conn.close()
