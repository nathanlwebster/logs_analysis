# logs_analysis

Logs analysis project for Nathan Webster for the Udacity Full Stack Nanodegree.

This project should be used with the newsdata.sql file provided with the nanodegree project files, with the database "news". 

Before running news.py, please create the following view:

create view totals as select date_part('month', time) as month, date_part('day', time) as date, count(status) from log group by date, month order by date;
