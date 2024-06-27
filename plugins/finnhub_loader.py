import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="<input your API here>")

    news = finnhub_client.general_news('general', min_id=0)

    return news
