import psycopg2


def connect():
    return psycopg2.connect("dbname=news")

if __name__ == '__main__':
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""select count(log.path),articles.title from articles
    inner join log on log.path ilike '%'|| articles.slug || '%' group by
    articles.title order by count(log.path) desc limit 3;""")
    most = cursor.fetchall()
    print "What are the most popular three articles of all time?"
    print "\n"
    for row in xrange(len(most)):
        print "\"", most[row][1], "\"---", most[row][0], " views."
    print "\n"
    cursor.execute("""select au.name, count(loges.path) from authors au
    inner join articles ar on au.id = ar.author inner join log loges
    on loges.path ilike '%' || ar.slug || '%' group by au.name
    order by count(loges.path) desc;""")
    most_authors = cursor.fetchall()
    print "Who are the most popular article authors of all time?"
    print "\n"
    for row in xrange(len(most_authors)):
        print ("\"%s\" -- %s views." % (most_authors[row][0],
               most_authors[row][1]))
    print "\n"
    print "On which days did more than 1% of requests lead to errors?"
    print "\n"
    cursor.execute("""select time::date,100.0 * sum(case when
    status='404 NOT FOUND' THEN 1 ELSE 0 END)/COUNT(*) as xx from log
    group by time::date order by xx desc limit 1;""")
    most_article = cursor.fetchall()
    for row in xrange(len(most_article)):
        print ("\"%s\" -- %.2f%%" % (most_article[row][0],
               most_article[row][1]))
    print "\n"
    connection.close()