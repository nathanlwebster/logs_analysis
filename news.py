import psycopg2

def question1():
    conn = psycopg2.connect(dbname="news")
    cursor = conn.execute("SELECT articles.title, count(articles.title) as num from log, articles where substr(log.path, 10, 30) = articles.slug group by articles.title order by num desc limit 3;")
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    question1()