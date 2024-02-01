
# Data Pipelines Using Apache AirFlow
## Task 1 - Define the DAG arguments
Create a DAG with these arguments.

owner
start_date
email
You may define any suitable additional arguments.
## Task 2 - Define the DAG
Create a DAG named process_web_log that runs daily.
Use suitable description.

![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/task1.png)

## Task 3 - Create a task to extract data
Create a task named extract_data.

This task should extract the ipaddress field from the web server log file and save it into a file named extracted_data.txt


## Task 4 - Create a task to transform the data in the txt file
Create a task named transform_data.

This task should filter out all the occurrences of ipaddress “198.46.149.143” from extracted_data.txt and save the output to a file named transformed_data.txt.

## Task 5 - Create a task to load the data
Create a task named load_data.

This task should archive the file transformed_data.txt into a tar file named weblog.tar.

![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/task2.png)

## Task 6 - Define the task pipeline
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/task3.png)

## Task 7 - Submit the DAG
### list all dags
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/listdags.png)
### check for process_web_log dag
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/checkdag.png)
### list tasks in process_web_log dag
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/pausedag.png)

## Task 8 - Unpause the DAG
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/listtask.png)
## Task 9 - Monitor the DAG
![](https://github.com/munna710/data-enginering-capstone-project/blob/main/Data%20Pipelines%20Using%20Apache%20AirFlow/images/monitor.png)

