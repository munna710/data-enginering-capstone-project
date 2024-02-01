# Task 1 - Create a database.
Create a database named sales.
## CREATE DATABASE sales;

# Task 2 - Design a table named sales_data.
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/sampledata.png)
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/createtable.png)
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/insert.png)
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/afterinsert.png)
# Task 3 - Import the data in the file oltpdata.csv
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/import.png)
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/afterimport.png)
# Task 4 - List the tables in the database sales
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/listtables.png)
# Task 5. Write a query to find out the count of records in the tables sales_data.
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/countrecords.png)
# Set up Admin tasks
# Task 6 - Create an index
Create an index named ts on the timestamp field.

![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/createindex.png)
# Task 7 - List indexes
List indexes on the table sales_data.
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/listindex.png)

# Task 8 - Write a bash script to export data.
- [datadump.sh](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/datadump.sh) that exports all the rows in the sales_data table to a file named sales_data.sql
- ![](https://github.com/munna710/data-enginering-capstone-project/blob/main/OLTP%20Database/images/export.png)
  
