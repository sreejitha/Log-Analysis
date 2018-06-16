## Pre-Requisites

Have the following view created in the news database. The command for which is
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

1> Clone this repository using the github link above


## Running application
1. cd into the /vagrant/news folder. If you are at the right place you will
see 2 files inside the folder- news.py, readme.md (this file)
2.Type the following command on terminal

```
python news.py
```
3. The console should display in sequence what questions the
results are answering and then the results themselves.
