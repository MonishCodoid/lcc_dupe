import mysql.connector
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *


def connect_db():
    connection = mysql.connector.connect(host="localhost",
                                         database="framework",
                                         user="root",
                                         password="Codoid@123")
    return connection


@lcc.test()
def test_dupe():
    cn = connect_db()
    cursor = cn.cursor()
    cursor.execute("SELECT first_name,COUNT(*) as count FROM employees GROUP BY first_name HAVING count > 1")
    a = cursor.fetchall()
    b = len(a)
    check_that('b', b, equal_to(1))
