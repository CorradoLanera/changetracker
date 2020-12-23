import sqlite3

from src.filechanges import get_base_file, connect_db


def test_get_base_file():
    db_file = get_base_file()
    assert db_file == "filechanges"


def test_connect_db():
    con = connect_db()
    assert isinstance(con, sqlite3.Connection)
