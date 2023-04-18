import psycopg2
import csv
con = psycopg2.connect(host = "localhost", database = "phonebook", user = "postgres", password = "kukamerey26")
current = con.cursor()

insert = """
    INSERT INTO PhoneBook VALUES(%s,%s,%s) returning *;
"""

update = """
    UPDATE PhoneBook SET number = %s WHERE name = %s;
"""

select = """
    SELECT * FROM PhoneBook
"""

delete = """
    DELETE FROM PhoneBook WHERE name = %s;
"""

while True:
    n = int(input(" 1 - insert csv, 2 - insert console, 3 - update, 4 - select, 5 - delete, 6 - exit\n"))
    if n == 1:
        with open("p4.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    current.execute(insert, row)
        con.commit()
    if n == 2:
            name = input("Name:")
            surname = input("Sname:")
            phoneNumber = input("Number:")
            current.execute(insert, (name, surname, phoneNumber))
            con.commit()
            
    if n == 3:
        name = input("Name:")
        phone_number = input("newnumber:")
        current.execute(update, (phone_number,name))
        con.commit()
    if n == 4:
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        con.commit()
    if n == 5:
        name = input("Name:")
        current.execute(delete, [name])
        con.commit()
    if n == 6:
        break


current.close()
con.commit()
con.close()