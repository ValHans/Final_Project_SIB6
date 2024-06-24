import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cpsotm9r01qpk40rgm50cpsotm9r01qpk40rgm5g")

    news = finnhub_client.general_news('general', min_id=0)

    return news
