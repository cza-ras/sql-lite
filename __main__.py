from db_functions import funkcje_bazy

baza = 'SQL/sql-lite/testowa.db'

#przykladowe polecenia
polecenie_select = "SELECT * FROM nazwiska WHERE nazwisko='Nowak'"
polecenie_insert = "INSERT INTO nazwiskaX VALUES ('Jan', 'Nowak', 30)"
polecenie_create = "CREATE TABLE nazwiskaX (imie text, nazwisko text, wiek integer)"

funkcje_bazy.polecenie_sql(baza_danych=baza, wyrazenie_sql=polecenie_select)