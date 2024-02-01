# Import libraries required for connecting to MySQL
import mysql.connector

# Import libraries required for connecting to DB2
import ibm_db

# Connect to MySQL
def connect_to_mysql():
    connection = mysql.connector.connect(
        user='root',
        password='MTk2MTgtdGhpc2lz',
        host='127.0.0.1',
        database='sales'
    )
    return connection

# Connect to DB2
def connect_to_db2():
    dsn_hostname = "b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
    dsn_uid = "rlf38431"
    dsn_pwd = "sGPzQuzBWJatBbVe"
    dsn_port = "32304"
    dsn_database = "bludb"
    dsn_driver = "{IBM DB2 ODBC DRIVER}"
    dsn_protocol = "TCPIP"
    dsn_security = "SSL"

    dsn = (
        "DRIVER={0};"
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID={5};"
        "PWD={6};"
        "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

    connection = ibm_db.connect(dsn, "", "")
    return connection

# Get last rowid from DB2
def get_last_rowid(connection):
    SQL = "SELECT MAX(rowid) FROM products"
    stmt = ibm_db.exec_immediate(connection, SQL)
    result = ibm_db.fetch_tuple(stmt)
    return result[0] if result else 0

# Get latest records from MySQL
def get_latest_records(connection, last_row_id):
    SQL = f"SELECT * FROM products WHERE rowid > {last_row_id}"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(SQL)
    return cursor.fetchall()

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database.

def insert_records(connection, records):
    SQL = "INSERT INTO products(rowid, product, category) VALUES(?, ?, ?)"
    stmt = ibm_db.prepare(connection, SQL)

    for record in records:
        ibm_db.execute(stmt, (record['rowid'], record['product'], record['category']))

# Disconnect from MySQL
def disconnect_from_mysql(connection):
    connection.close()

# Disconnect from DB2
def disconnect_from_db2(connection):
    ibm_db.close(connection)

# Main program
if __name__ == "__main__":
    # Connect to MySQL
    mysql_connection = connect_to_mysql()

    # Connect to DB2
    db2_connection = connect_to_db2()

    # Get last rowid from DB2
    last_row_id = get_last_rowid(db2_connection)

    # Get latest records from MySQL
    new_records = get_latest_records(mysql_connection, last_row_id)

    print("New rows on staging data warehouse =", len(new_records))

    # Print the new records
    print("New records:", new_records)

    # Insert records into DB2
    insert_records(db2_connection, new_records)

    print("New rows inserted into production data warehouse =", len(new_records))

    # Disconnect from MySQL
    disconnect_from_mysql(mysql_connection)

    # Disconnect from DB2
    disconnect_from_db2(db2_connection)