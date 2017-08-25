import psycopg2
import calendar


def question1():
    conn = psycopg2.connect(dbname="news")
    cursor = conn.cursor()
    cursor.execute("SELECT articles.title, count(articles.title) as num" +
                   "from log, articles where substr(log.path, 10, 30) =" +
                   "articles.slug group by articles.title order by num desc" +
                   "limit 3;")
    results = cursor.fetchall()
    print("\n\n")
    print("\nWhat are the most popular three articles of all time?")
    for result in results[:3]:
        print("\n\"" + str(result[0]) + "\" -- " + str(result[1]) + " views")
    conn.close()
    return results


def question2():
    conn = psycopg2.connect(dbname="news")
    cursor = conn.cursor()
    cursor.execute("SELECT authors.name, count(authors.name) as num from" +
                   "log, authors, articles  where substr(log.path, 10, 30)" +
                   " = articles.slug and authors.id = articles.author group" +
                   " by authors.name order by num desc;")
    results = cursor.fetchall()
    print("\n")
    print("\nWho are the most popular article authors of all time?")
    for result in results[:3]:
        print("\n\"" + str(result[0]) + "\" -- " + str(result[1]) + " views")
    conn.close()
    return results


def question3():
    conn = psycopg2.connect(dbname="news")
    cursor = conn.cursor()
    cursor.execute("select totals.month, totals.date, date_part('year', " +
                   "time) as year, 100.0 * count(log.*)/totals.count as " +
                   "percent_error from log, totals where date_part('day'," +
                   " time) = totals.date and log.status = '404 NOT FOUND'" +
                   " group by totals.date, totals.count, totals.month, year" +
                   " having 100.0 * count(log.*)/totals.count > 1;")
    results = cursor.fetchall()
    month = int(results[0][0])
    day = str(int((results[0][1])))
    year = str(int(results[0][2]))
    percent = str(round((results[0][3]), 2))

    print("\n\n")
    print("\nOn which days did more than 1% of requests lead to errors?")
    print("\n" + calendar.month_name[month] + " " + day +
          ", " + year + " -- " + percent + "%")
    conn.close()
    print("\n\n")
    return results

if __name__ == "__main__":
    question1()
    question2()
    question3()
