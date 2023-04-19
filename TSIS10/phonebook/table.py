import psycopg2


def create_table():
    command = (
        '''
        CREATE TABLE PhoneBook(
            name VARCHAR (255) UNIQUE NOT NULL,
            surname VARCHAR (12) NOT NULL,
            number VARCHAR (12) NOT NULL
        );
        '''
    )
    try:   
        con = psycopg2.connect(host = "localhost", database = "phonebook", user = "postgres", password = "kukamerey26")
        current = con.cursor()
        current.execute(command)
        current.close()
        con.commit()

    except Exception as E:
        print(str(E))
    if con is not None:
        con.close()


create_table()