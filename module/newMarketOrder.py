from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import logging
from variables import globalVar
from binanceAPI.teleBot import send_error

# NEW MARKET ORDER
def newMarketOrder(symbol,positionSide,side,type,quantity): 
    try:
        response = um_futures_client.new_order(
            symbol = symbol,
            positionSide = positionSide,
            side = side,
            type = type,
            quantity = round(quantity,globalVar.quantityPrecision)
        )
        #logging.info(response)
    except ClientError as error:
        send_error("Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            ))
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )