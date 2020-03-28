import yfinance as yf
import time
import matplotlib.pyplot as plt


TICKER_LIST = ['ES=F', 'MSFT']


"""
To provide ideas which applications we do have in mind. Instead of using established numerical algorithms one can learn solutions from observations.
Deep Hedging (Bühler-Gonon-Teichmann-Wood 2017)
Deep Calibration (Cuchiero-Teichmann et al. 2016-17-18)
Deep Simulation (Cuchiero-Gonon-Grigoryeva-Ortega 2019)
What is Hedging? Solutions of non-linear, non-standard optimization problems.
What is Calibration? Model selection given certain market data.
What is simulation? Prediction of time series.
All tasks of tremendous importance in every day finance.
"""


def refresh_input(ticker_list = TICKER_LIST, period='1d', interval='1m'):
    # Todo: Implement function to update input data
    states = {}
    for t in ticker_list:
        ticker = yf.Ticker(t)
        hist = ticker.history(period=period, interval=interval)
        dates = hist.index.values
        start = dates[0]
        steps = dates - start
        High = hist["High"].to_numpy()
        Low = hist['Low'].to_numpy()
        additional_info = ''  # some news-feed info?
        # print(additional_info)
        states.update({'time': steps, t: {'history': {'High': High, 'Low': Low}, 'info': additional_info}})
    return states


class HedgeHawk:
    def __init__(self, refresh_rate=1,
                 plot_states=True):
        self.refresh_rate = refresh_rate  # how often are stats refreshed
        idx = 0
        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        plt.ion()
        while(True):
            idx += 1
            self.states = states = refresh_input()
            print(idx)
            if plot_states:
                self.visualize_states()
            time.sleep(self.refresh_rate)
        
    def portfolio_optimization(self):
        pass

    def visualize_states(self, show_idx=0):
        idx = TICKER_LIST[show_idx]
        df = self.states[idx]
        high = df['history']['High']
        print(high.shape)
        low = df['history']['Low']
        length = low.shape[0]
        print(low.shape)
        t = self.states['time'][:length].astype(float)
        high=high[:t.shape[0]]
        low=low[:t.shape[0]]
        print(t.shape)
        plt.plot(t, high)
        plt.plot(t, low)
        self.fig.canvas.draw()
        image = np.fromstring(self.fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        image = image.reshape(self.fig.canvas.get_width_height()[::-1] + (3,))
        
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
   

    def visualize_portfolio():
        pass


class Portfolio:
    def __init__():
        self.info = 'test portfolio'
       
    def visualize(self):
        pass


HedgeHawk()