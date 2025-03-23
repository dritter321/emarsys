# SQL assigment tasks

Your company sends marketing emails to it’s users.
You have a database table containing information about email sends from the company to 
the users. The table has the following schema:

| Field name   | Type       | Description                            |
|--------------|------------|----------------------------------------|
| campaign_id  | Integer    | ID of the marketing email campaign.    |
| user_id      | Integer    | ID of the user.                       |
| event_time   | Timestamp  | Send time of the marketing campaign.  |

## Task 1
Write a query that counts the number of emails sent for each campaign.

## Task 2
Write a query that counts the number of emails sent each week in the last half year.

----------------------------------------------------------------------------------------------------------------------------

You have another table containing information which emails have been opened by the user.
The table has the following schema:

| Field name   | Type       | Description                         |
|--------------|------------|-------------------------------------|
| campaign_id  | Integer    | ID of the marketing email campaign. |
| user_id      | Integer    | ID of the user.                     |
| event_time   | Timestamp  | Time of opening the email.          |

## Task 3
Write a query that calculates the open rate of each campaign.


# Local Testing
You can create, populate, and verify SQLite database with the two tables needed with the following command:
`python create_sqlite_marketing_data_db.py`
You can then run the queries on the database using the following commands:
`python execute_task_01.py`
`python execute_task_02.py`
`python execute_task_03.py`