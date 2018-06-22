## About Log Analysis
The Log Analysis project is an internal reporting tool which looks at the
database of a newspaper website to understand what articles the readers like.
The database has 3 tables- articles, authors and log. The articles table has a
row for every article that is on the website. The authors table is about the
authors who wrote these articles. The log table has a row for each time a
reader looked at a page on the news website. These tables have primary key-
foreign key relationships amongst each other. This internal reporting tool is
a console program in python
which connects to the postgres database (using psycopg2 adapter)
which is the backend for the newspaper website, analyses it and prints out
answers to 3 very specific questions that were asked. This program does not
take any user input.

The questions answered are:
1> What are the most popular three articles of all time?
2> Who are the most popular article authors of all time?
3> On which days did more than 1% of requests lead to errors?


## Setup before running the application
1> Have [Virtualbox](https://www.virtualbox.org/wiki/VirtualBox) & [Vagrant](https://www.vagrantup.com/intro/index.html)
installed into your computer suiting the environment you are running the
program in. Download links:
1>[Virtualbox] (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2>[Vagrant](https://www.vagrantup.com/downloads.html)

Once you have the VM installed, you must use Vagrant to launch it and not
VirtualBox (instructions on that are in a few steps)

2> Download and install the VM Configuration:
This VM comes with postgres database that is to be analyzed
and other important packages
such as [Flask] (http://flask.pocoo.org/)
& [psycopg2] (http://initd.org/psycopg/). Download link for VM Configuration:
[VM Config](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
NOTE:We are not actually using Flask in this project as there is no user input.

Psycopg2 is the Postgres Adapter we are using to connect the database with our
console program written in python.

3> ### Download the code
Clone this repository into the vagrant folder using the github link above
4> Start the VM using Vagrant:
From the terminal inside the vagrant subdirectory (which is the directory below
 'FSND-Virtual Machine') type
```
vagrant up
```
and enter into the new VM using
```
vagrant ssh
```
4> cd into the vagrant folder using
```
cd /vagrant
```

5> Download the sql data and unzip it into the vagrant folder from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Load the data into the database using
```
psql -d news -f newsdata.sql
```

Ensure that the database has been created successfully and that you can connect
to it using ```psql -d news```
6> Have the following view created in the news database. The command for which is
as follows:
```
CREATE VIEW ERROR_SUM_DAY AS
select date(time) AS ERR_DATE, SUM(CASE WHEN status LIKE '4%' THEN 1
WHEN status LIKE '5%' THEN 1 ELSE 0 END):: DECIMAL/COUNT(date(time)) AS
ERR_RATIO
from log
group by ERR_DATE;
```
Exit out of psql using the following command on the terminal
```
\q
```

## Running application
1> Assuming you have followed the steps in Setup and are still logged in into
the VM,
cd into the /vagrant/Log-Analysis folder in the terminal where your VM is
running. If you are at the right place you will see 3 files inside the folder-
news.py, output.txt & readme.md (this file)

2> Type the following command on terminal from the Log-Analysis folder

```
python news.py
```
3> The console should display in sequence what questions the
results are answering and then the results themselves.

4> If you see some errors related to packages being missing (which shouldn't ideally happen
because these files are the exact same)
while running the application or while connecting to the database
from the terminal, then you can replace  your VagrantFile which is under FSND-Virtual-Machine/vagrant with the one [here]
(https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)


## About the solution itself

I've used joins and group by clause to answer the first 2 queries. The reason
for this is the data requested was in multiple tables related to each other
via foreign key/ primary key.The group by was used to aggregate on the count.

For the 3rd question, I first created a view to get the error ratio grouped
by day. Then I wrote a select query over this view to get the percentage in
order to keep the queries readable.
