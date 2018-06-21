#!/usr/bin/env python
""" Console Program for log analysis """
import psycopg2
DBNAME = "news"


def get_db_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


"""Following query is for top 3 popular articles """
query_popular_articles = ''.join([
                         'select a.title as title, count(*) as count',
                         ' from articles a join log b on b.path= \'/article/\''
                         ' ||a.slug',
                         ' group by a.title',
                         ' order by count(*) desc',
                         ' limit 3;'])

"""Following query is for popular authors ranked in descending order"""
query_popular_authors = ''.join([
                        'select au.name, count(*)',
                        ' from authors au join articles a on au.id = a.author'
                        ' join log b on b.path = \'/article/\' ||a.slug'
                        ' group by au.name'
                        ' order by count(*) desc;'])

"""Following query is for days having greater than 1 percent request errors"""
query_high_error_rate = ''.join([
                        'select TO_CHAR(esd.ERR_DATE,',
                        '\'Month dd, yyyy\'),',
                        ' ROUND(100.0 * (esd.ERR_RATIO),1)',
                        ' from ERROR_SUM_DAY AS esd',
                        ' group by esd.ERR_DATE, esd.ERR_RATIO',
                        ' having ROUND(100.0 * (esd.ERR_RATIO),1) > 1;'
                        ])


def get_three_articles():
    articles = get_db_results(query_popular_articles)
    print("Most popular 3 articles of all time are:\n")
    for x in articles:
        print ''.join([
              '"', x[0], '"', '--', str(x[1]), ' views'
              ])


def get_popular_authors():
    authors = get_db_results(query_popular_authors)
    print("\nMost popular article authors of all time are:\n")
    for x in authors:
        print ''.join([
                      x[0], '--', str(x[1]), ' views'
                      ])


def get_days_high_error_rate():
    days = get_db_results(query_high_error_rate)
    print("\nDays when more than 1 percent requests led to errors:\n")
    for x in days:
        print ''.join([
                      ' '.join(x[0].split()), '--', str(x[1]), '% errors'
                      ])


def main():
    get_three_articles()
    get_popular_authors()
    get_days_high_error_rate()


if __name__ == "__main__":
    main()
