import os
import sqlite3


def get_base_file():
    """Returns the name of the SQLite DB file"""
    return os.path.splitext(os.path.basename(__file__))[0]


def connect_db():
    """Connects to the SQLite DB"""
    db_file = get_base_file() + '.db'

    try:
        return sqlite3.connect(db_file, timeout=2)
    except:
        print("Connection error to " + db_file)
        return False


if __name__ == "__main__":
    print("Base file is: " + get_base_file() + ".")

    con = connect_db()
    print(type(con))
    c = con.cursor()
    c.execute("DROP TABLE if EXISTS people;")
    print(c.fetchall())
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())
    c.execute("CREATE TABLE people (id integer primary key, name text, count integer);")
    print(c.fetchall())
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())
    c.execute("DROP TABLE people;")
    print(c.fetchall())
    con.close()
