## Pre-Requisites
1> Have virtualbox & vagrant installed into your computer. Vagrant can be downloaded
from vagrantup.com

2> Download and install the VM pre-configured with postgres and other
important packages such as flask, oauth2client etc from [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)

3> Bring the VM online using
```
vagrant up
```
and ssh into the new VM using
```
vagrant ssh
```
4> cd into the vagrant using
```
cd /vagrant
```

6> Download the sql data and unzip it into the vagrant folder from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Load the data into the database using
```
psql -d news -f newsdata.sql
```

Ensure that the database has been created successfully and that you can connect
to it using ```psql -d news```

7> Have the following view created in the news database. The command for which is
as follows:
```
CREATE VIEW ERROR_SUM_DAY AS
select date(time) AS ERR_DATE, SUM(CASE WHEN status LIKE '4%' THEN 1
WHEN status LIKE '5%' THEN 1 ELSE 0 END):: DECIMAL/COUNT(date(time)) AS
ERR_RATIO
from log
group by ERR_DATE;
```

## Downloading Code

1> Clone this repository into the vagrant folder using the github link above


## Running application
1> cd into the /vagrant/Log-Analysis folder. If you are at the right place you will
see 3 files inside the folder- news.py, output.txt & readme.md (this file)

2> Type the following command on terminal

```
python news.py
```
3> The console should display in sequence what questions the
results are answering and then the results themselves.

### About the solution itself

I've used joins and group by clause to answer the first 2 queries. The reason for this is the
data requested was in multiple tables related to each other via foreign key/ primary key.
The group by was used to aggregate on the count.

For the 3rd question, I first created the view to get the error ratio grouped by day. Then I wrote a select query over this view to get the percentage in order to keep the queries readable.
