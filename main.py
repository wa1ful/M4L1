import sqlite3

db_path = 'movie.db'

def execute_query(query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

query1 = """
SELECT title, budget 
FROM movies 
ORDER BY popularity DESC 
LIMIT 1;
"""
result1 = execute_query(query1)
print(result1[0][1])

query2 = """
SELECT title 
FROM movies 
WHERE release_date LIKE '2009-12%' 
ORDER BY budget DESC 
LIMIT 1;
"""
result2 = execute_query(query2)
print(result2[0][0])

query3 = """
SELECT title 
FROM movies 
WHERE tagline = 'The battle within.';
"""
result3 = execute_query(query3)
print(result3[0][0])

query4 = """
SELECT title, vote_count 
FROM movies 
WHERE release_date < '1980-01-01' AND vote_average > 8 
ORDER BY vote_count DESC 
LIMIT 1;
"""
result4 = execute_query(query4)
print(result4[0][0])
