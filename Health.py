#Health Data
import sqlite3

db = sqlite3.connect('test4.sqlite')
db.execute("""CREATE TABLE IF NOT EXISTS test4 
            (id INTEGER,
            date TEXT,
            test TEXT, 
            range TEXT,
            result REAL)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (1, '2017-10-30', 'WBC', '3.9-10.3 K UL', 6.1)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (2, '2017-10-30', 'RBC', '4.34-5.61 M UL', 5.12)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (3, '2017-10-30', 'HGB', '12.6-17.0 g dbl', 15.6)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (4, '2017-10-30', 'HCT', '37.8-51%', 45.5)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (5, '2017-10-30', 'MCV', '82.0-98.4 fL', 88.8)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (6, '2017-10-30', 'MCH', '25.7-33.8 pg', 30.4)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (7, '2017-10-30', 'MCHC', '32.0-36.0 G DL', 34.3)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (8, '2017-10-30', 'RDW', '11.5-15.5%', 12.4)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (9, '2017-10-30', 'PLT', '150-400 K UL', 253)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (10, '2017-10-30', 'MPV', '7.4-10.4 fL', 7.7)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (11, '2017-10-30', 'Glu', '80-117 mg dL', 109)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (12, '2017-10-30', 'BUN', '7-25 mg dL', 9)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (13, '2017-10-30', 'Creat', '0.5-1.5 mg dL', 1.2)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (14, '2017-10-30', 'BUN/Creat', '6-20', 8)""")
db.execute("""INSERT INTO test4 
            (id, date, test, range, result) VALUES (15, '2017-10-30', 'Calcium', '8.5-10.8 mg dL', 9.5)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (16, '2017-10-30', 'Na', '135-148 meq L', 141)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (17, '2017-10-30', 'K', '3.5-5.3 men L', 5.0)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (18, '2017-10-30', 'Cl', '100-112 meq L', 102)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (19, '2017-10-30', 'CO2', '23-30 meq L', 27)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (20, '2017-10-30', 'TP', '6.3-7.9 g dl', 7.2)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (21, '2017-10-30', 'Alb', '3.7-4.5 g dl', 4.3)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (22, '2017-10-30', 'A/G', '1.0-2.4', 1.5)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (23, '2017-10-30', 'TBili', '0.0-1.0 mg dL', .4)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (24, '2017-10-30', 'AlkPhos', '31-155 U L', 69)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (25, '2017-10-30', 'AST', '0-40 U L', 19)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (26, '2017-10-30', 'ALT', '0-50 U L', 24)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (27, '2017-10-30', 'Anion', '10-20', 17)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (28, '2017-10-30', 'GFR', '<60 mL min', 65)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (29, '2017-10-30', 'Chol', '0-200 mg dL', 249)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (30, '2017-10-30', 'Trig', '30-150 mg dL', 116)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (31, '2017-10-30', 'HDL', '36-100 mg dL', 58)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (32, '2017-10-30', 'LDL', '0-130', 168)""")
db.execute("""INSERT INTO test4
            (id, date, test, range, result) VALUES (33, '2017-10-30', 'VLDL', '0-39', 23)""")

cursor = db.cursor()
cursor.execute("SELECT * FROM test4")

print('{0:10}{1:20}{2:20}{3:10}{4:15}'.format('ID','date','test','range','result'))
for id, date, test, range, result in cursor:
    print('{0:3}{1:20}{2:20}{3:10}{4:15}'.format(id,date,test,range,result))

cursor.close()
db.close()


