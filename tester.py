import requests
import random


class Tester:
    def __init__(self):
        self.name = "Tester"

    def get_params(self):
        return {
            #### DIVERGENCE PARAMETERS ####
            "Left Bars": {"min": 4, "max": 11, "step": 1},
            "Right Bars": {"min": 4, "max": 11, "step": 1},
            "Minimum Number of Divergence": {"min": 1, "max": 10, "step": 1},
            "Minimum Number of Bar for Divergence": {"min": 1, "max": 20, "step": 1},
            #### INDICATORS PARAMETERS ####
            "RSI": {"min": 0, "max": 3, "step": 1},
            "MACD": {"min": 0, "max": 3, "step": 1},
            "MACD Histogram": {"min": 0, "max": 3, "step": 1},
            "Momentum": {"min": 0, "max": 3, "step": 1},
            "CCI": {"min": 0, "max": 3, "step": 1},
            "Stochastic": {"min": 0, "max": 3, "step": 1},
            "Diosc": {"min": 0, "max": 3, "step": 1},
            "VWmacd": {"min": 0, "max": 3, "step": 1},
            "Chaikin Money Flow": {"min": 0, "max": 3, "step": 1},
            "Money Flow Index": {"min": 0, "max": 3, "step": 1},
            "OBV": {"min": 0, "max": 1, "step": 1},
            #### TAKE PROFIT AND STOP LOSS PARAMETERS ####
            "Min Take Profit": {"min": 0.8, "max": 1.5, "step": 0.2},
            "Max Take Profit": {"min": 2, "max": 5, "step": 0.2},
            "TP Decrease rate": {"min": 0.4, "max": 1.5, "step": 0.1},
            "Max Stop Loss": {"min": 30, "max": 40, "step": 1},
            "Min Stop Loss": {"min": 15, "max": 20, "step": 1},
            "SL Decrease rate": {"min": 0.01, "max": 0.1, "step": 0.01},
            "Free Tradable 1/n of Pyramiding": {"min": 2, "max": 4, "step": 1},
            "Wait for green bar": {"min": 0, "max": 1, "step": 1},
            #### ATR PARAMETERS ####
            "Activate ATR Mult.": {"min": 2, "max": 7, "step": 1},
            "Offset ATR Mult": {"min": 3, "max": 7, "step": 1},
            #### DISABLED PARAMETERS ####
            # "Pyramiding": {"min": 1, "max": 10},
            # "ATR Length": {"min": 10, "max": 14}
        }


    def get_random_params(self, params):
        # Get random params from the params dictionary according to the step
        random_params = {}
        for key in params.keys():
            min_val = params[key]["min"]
            max_val = params[key]["max"] 
            step = params[key]["step"]
            
            # Calculate number of possible steps
            num_steps = int((max_val - min_val) / step)
            
            # Get random number of steps
            random_steps = random.randint(0, num_steps)
            
            # Calculate random value according to step size
            random_val = min_val + (random_steps * step)
            
            random_params[key] = random_val
            
        return random_params
   
    def test(self, params):
        # Send params to the tester api
        response = requests.post("https://36e3-31-223-43-241.ngrok-free.app/api/cycle/", 
                                 headers={"Content-Type": "application/json", "port":"12025"},
                                 json={
            "strategy": "DivV6",
            "parameters": params,
        })
        
        if(response.status_code == 200):
            result = response.json()["results"]
            if(result != 1):
                score = result["Net Profit %: All"] / result["Max Drawdown %"]
            else:
                score = -1
        else:
            score = -1

        return score