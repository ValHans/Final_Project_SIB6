1. Run Airflow using `docker-compose up`
2. Create Plugins:
    - Finnhub loader
    - MongoDB loader
    - Sentiment Analysis
    - Postgres loader
3. Create python code to extract from Finnhub and load to MongoDB 
4. Create Python code that Get data from MongoDB and do Sentiment Analysis then load the result to Postgres 
    - (mongodb_loader, finnhub_loader, finnhub_mongodb_loader)

5. Result from trying this project
    - ![Result 1](screenshot\sentiment_news_analysis.jpeg)
    - ![Result 2](screenshot\dags_sentiment_analysis.jpeg)
