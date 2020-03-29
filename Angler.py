import yfinance as yf
import time
import matplotlib.pyplot as plt


TICKER_LIST = ['ES=F', 'MSFT']


class Angler:
    def __init__(topic = 'Coronavirus',
                 n = 10,
                 enrichment = 100,
                 ):
        self.info = 'test portfolio'
        self.topic = ''
        # Given a topic etc find a list of interesting entities (either negative or positive economic impact)
        self.bucket = {}

    def get_content(self):
        # Find a list of entities related to the topic
        # Summarize 
        pass

    def nlp(self):
        # Use Bert to create a summary
        # Use Bert to create an embedding
        pass

    def cluster(self):
        # cluster the created embeddings
        pass

    def get_bucket(self):
        return 
