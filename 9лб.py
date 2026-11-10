db = []
data = [
    ('9844720488', 'E340BT', 77, 'Lada Granta', 'Красный', 87, 2017, 35),
    ('6239572784', 'H1090K', 178, 'Volkswagen Polo', 'Синий', 15, 2018, 40),
    ('6239572784', 'A822EY', 99, 'Skoda Rapid', 'Черный', 125, 2021, 35),
    ('7984672834', 'T120AA', 98, 'Hyundai Solaris', 'Черный', 123, 2019, 20),
    ('7478679847', 'B971HP', 199, 'Kia Sportage', 'Белый', 184, 2017, 35),
    ('4728472878', 'T120AA', 77, 'Toyota RAV4', 'Серебристо-серый', 146, 2008),
    ('4782487387', 'H454EE', 98, 'Skoda Rapid', 'Черный', 75, 2021, 0),
    ('9884274842', 'O638OA', 173, 'Mitsubishi Outlander', 'Белый', 230, 2021), 
    ('7284728297', 'T120AA', 77, 'Hyundai Solaris', 'Синий', 123, 2021, 0),
    ('8779854025', 'A352EE', 98, 'Lada Granta', 'Белый', 87, 2017, 54)
]

for i, row in enumerate(data, 1):
    reg, curn, region, power = row[0], row[1], row[2], row[5]
    
    if (len(row) != 8 or power <= 50 or 
        any(x[0] == reg for x in db) or 
        any(x[1] == curn and x[2] == region for x in db)):
        
        print(f"Команда {i}: Ошибка")
    else:
        db.append(row) 
        print(f"Команда {i}: Добавлено: {row[3]}, цвет {row[4]}")
print(f"\nВсего успешных вставок: {len(db)}")