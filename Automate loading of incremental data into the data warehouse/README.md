# Create a database named sales in mysql and Import the data in the file sales.sql into the sales database.
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Automate%20loading%20of%20incremental%20data%20into%20the%20data%20warehouse/images/mysqlcon.png)
# If you choose DB2 as the data warehouse:
- Step 1: Download the db2connect.py python program from the link below.

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/db2connect.py

db2connect.py has the sample code to help you understand how to connect to the cloud instance of IBM DB2 using Python.

Note: Before executing db2connect.py note that you install the connector using the command pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3

Step 2: Modify db2connect.py suitably and make sure you are able to connect to your cloud instance of IBM DB2.
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Automate%20loading%20of%20incremental%20data%20into%20the%20data%20warehouse/images/db2con.png)
Step 3: Download the file below

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.csv

Step 4: Load sales.csv into a table named sales_data on your cloud instance of IBM DB2 database.
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Automate%20loading%20of%20incremental%20data%20into%20the%20data%20warehouse/images/loaddb2.png)
# Automate loading of incremental data into the data warehouse
One of the routine tasks that is carried out around a data warehouse is the extraction of daily new data from the operational database and loading it into the data warehouse.
## Task 1 - Implement the function get_last_rowid()
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Automate%20loading%20of%20incremental%20data%20into%20the%20data%20warehouse/images/t1.png)
## Task 2 - Implement the function get_latest_records()
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Automate%20loading%20of%20incremental%20data%20into%20the%20data%20warehouse/images/t2.png)
## Task 3 - Implement the function insert_records()
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Automate%20loading%20of%20incremental%20data%20into%20the%20data%20warehouse/images/t3.png)
## Task 4 - Test the data synchronization
Run the program automation.py and test if the synchronization is happening as expected.

![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Automate%20loading%20of%20incremental%20data%20into%20the%20data%20warehouse/images/sync.png)
