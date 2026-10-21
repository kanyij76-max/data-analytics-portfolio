# 🎬 Movie Database Analysis & Insights (SQL)

## 📌 Project Overview
This project focuses on querying a multi-table relational database to extract actionable insights regarding movie production budgets, release timelines, financial performance, and audience reviews. 

## 🛠️ Tech Stack & Tools
* **Database Language:** SQL (MySQL / PostgreSQL)
* **Key Operations:** `JOIN` clauses, `GROUP BY`, aggregate functions (`SUM`, `AVG`, `COUNT`), and subqueries.

## 🔍 Key Business Questions Explored
1. What are the top 10 highest-grossing movies relative to their production budgets?
2. How do release months impact average user ratings and box office returns?
3. Which genres consistently yield the highest return on investment (ROI)?

## 💻 Sample SQL Query
Here is an example of a query used to analyze average movie ratings by genre:
```sql
SELECT 
    genre,
    COUNT(movie_id) AS total_movies,
    ROUND(AVG(user_rating), 2) AS average_rating
FROM movies
JOIN ratings ON movies.movie_id = ratings.movie_id
GROUP BY genre
ORDER BY average_rating DESC;
