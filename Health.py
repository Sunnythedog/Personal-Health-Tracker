# health.py started 12/31/17 @ 12:40 pm revision 0.1
# Created to track my health

import sqlite3
import time

conn = sqlite3.connect('health.db')
c = conn.cursor()

# Blood Pressure menu selection for database input
def blood_pressure():

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

    create_table_blood_pressure()
    blood_pressure_dynamic_data_entry()
    read_from_db_blood_pressure()

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
        (date, WBC, RBC, HGB, HCT, MCV, MCH, MCH_C, RDW, PLT, MPV, Glu, BUN, BUNCreat, Calcium, Na, K, Cl, CO2, TP, Alb, AG, Tbili, AlkPhos, AST, ALT, Anion, GFR, Chol, Trig, HDL, LDL, VLDL))
        conn.commit()

    def read_from_db_blood_test():
        c.execute('SELECT * FROM blood_test')
        for row in c.fetchall():
            print(row)

    create_table_blood_test()
    blood_test_dynamic_data_entry()
    read_from_db_blood_test()

    main_menu()

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

def main_menu(): # Main Menu
    print('')
    print('1 - Blood Pressure')
    print('2 - Blood Test Results')
    print('3 - Weight, PWV, Bone Weight, Muscle Weight, Body Fat Percentage, Water')
    print('4 - Body Temperature')
    print('5 - Diet')
    print('6 - Exercise')
    print('7 - O2 Levels')
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
        print ('four')
    elif menu_selection == '6':
        print ('four')
    elif menu_selection == '7':
        print ('four')
    else:
        print ('Unknown option selected, please choose again')
        main_menu()
    print('')

main_menu()

c.close()
conn.close()
