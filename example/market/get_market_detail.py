import os
import sys
import pathlib
sys.path.append(str(pathlib.Path(os.path.abspath(__file__)).parent.parent.parent))
from huobi.client.market import MarketClient

market_client = MarketClient()
obj = market_client.get_market_detail("btcusdt")
obj.print_object()



