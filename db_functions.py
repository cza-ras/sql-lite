import sqlite3

class funkcje_bazy():

    def polecenie_sql(baza_danych, wyrazenie_sql):
        polaczenie = sqlite3.connect(baza_danych)
        print(f'podlaczono z baza danych o nazwie {baza_danych}')

        cursor = polaczenie.cursor()
        cursor.execute(wyrazenie_sql)
        print(cursor.fetchall())
        polaczenie.commit()
        print('wykonano polecenie SQL')

        polaczenie.close()
        print(f'rozlaczono z baza danych o nazwie {baza_danych}')

