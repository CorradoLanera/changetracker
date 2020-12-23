from src.filechanges import get_base_file
from src.filechanges import connect_db
import sqlite3

def test_get_base_file():
    db_file = get_base_file()
    assert db_file == "filechanges"


def test_connect_db():
    con = connect_db()
    assert isinstance(con, sqlite3.Connection)
