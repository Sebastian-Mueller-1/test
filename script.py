from array import array
from operator import index
import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
print("pre class start")
class EmergyModel():

    def __init__(self):
        
        # df for model output
        self.master_array = np.zeros(shape=(5001,5)) 
        
        # df for percent change method
        self.percent_change_df = pd.DataFrame({"": ["Baseline","k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"],
                   'GDP': ["1.14","", "", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"],
                   'Assets': ["159.65","k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"],
                   'Population': ["0.21","k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"], 
                   '% Change GDP': ["0%","k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"],
                   '% Change Assets': ["0%","k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"],
                   '% Change Population': ["0%","k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"]
                               })
        
        
        #init parameters
        self.para_dict = {'j': 8.560001, 
                           'dt': 0.1,
                           'n': 0.01,
                           'a': 1, 
                           'dA': 0,
                           'dF': 0,
                           'r': 12.5, 
                           'f': 600,
                           'k0': 0.000021,
                           'k1': 0.000017, 
                           'k2': 0.01, 
                           'k3': 0.000017, 
                           'k4': 0.01, 
                           'k5': 0.05,
                           'k6': 0.013,
                           'k7': 0.126, 
                           'k8': 0.004,
                           'k9': 0.009,
                           'k10': 0.0433,
                           'k11': 0.0011,
                           'k12': 0.005,
                           'k13': 0.01,
                           'P2': 0.1,
                           'P1': 0.5, 
                           't': 1850,
                           'sw1': 0,
                           'sw2': 0, 
                           'gdp': 0,
                           'counter': 0}
        
        # parameter init, for model reset
        self.para_dict_reference = {'j': 8.560001, 
                           'dt': 0.1,
                           'n': 0.01,
                           'a': 1, 
                           'dA': 0,
                           'dF': 0,
                           'r': 12.5, 
                           'f': 600,
                           'k0': 0.000021,
                           'k1': 0.000017, 
                           'k2': 0.01, 
                           'k3': 0.000017, 
                           'k4': 0.01, 
                           'k5': 0.05,
                           'k6': 0.013,
                           'k7': 0.126, 
                           'k8': 0.004,
                           'k9': 0.009,
                           'k10': 0.0433,
                           'k11': 0.0011,
                           'k12': 0.005,
                           'k13': 0.01,
                           'P2': 0.1,
                           'P1': 0.5, 
                           't': 1850,
                           'sw1': 0,
                           'sw2': 0, 
                           'gdp': 0,
                           'counter': 0}
        print("finished init")

    def run_model(self):
            print("enter model")
            # main model loop
            while self.para_dict['t'] < 2350:

                # trade conditions
                if self.para_dict['t'] > 1950:
                    self.para_dict['sw1'] = 1
                    self.para_dict['sw2'] = 1

                self.para_dict['r'] = self.para_dict['j'] / (1 + self.para_dict['k1'] * self.para_dict['f'] * self.para_dict['n'] * self.para_dict['a'] + (self.para_dict['k2'] * self.para_dict['a']))

                self.para_dict['dF'] = ((-1*self.para_dict['k0'])*self.para_dict['r']*self.para_dict['f']*self.para_dict['n']*self.para_dict['a'])-(self.para_dict['k12']*self.para_dict['f']*self.para_dict['sw1'])+(self.para_dict['P2']*(self.para_dict['k13']*self.para_dict['a']*self.para_dict['sw2']))

                self.para_dict['dA'] = self.para_dict['k3'] * self.para_dict['r'] * self.para_dict['f'] * self.para_dict['n'] * self.para_dict['a'] + self.para_dict['k4'] * self.para_dict['r'] * self.para_dict['a'] - self.para_dict['k5'] * self.para_dict['a'] - self.para_dict['k6'] * self.para_dict['a'] - self.para_dict['k10'] * self.para_dict['n'] * self.para_dict['n'] * (1 - self.para_dict['k9'] * self.para_dict['a']) - self.para_dict['k10'] * self.para_dict['n'] * (1 - self.para_dict['k9'] * self.para_dict['a']) - self.para_dict['k13'] * self.para_dict['a'] * self.para_dict['sw2'] + self.para_dict['P1'] * (self.para_dict['k12'] * self.para_dict['f'] * self.para_dict['sw1'])

                self.para_dict['b'] = self.para_dict['k11'] * (self.para_dict['a'] / self.para_dict['n']) * self.para_dict['n']

                self.para_dict['d'] = self.para_dict['k7'] * self.para_dict['n'] * (1 - self.para_dict['k9'] * self.para_dict['a']) + self.para_dict['k8'] * self.para_dict['n'] * self.para_dict['n'] * (1 - self.para_dict['k9'] * self.para_dict['a'])
                if self.para_dict['d']<0:
                    self.para_dict['d']=0

                self.para_dict['f'] = self.para_dict['f'] + self.para_dict['dF']*self.para_dict['dt']  

                self.para_dict['n'] = self.para_dict['n']+(self.para_dict['b']-self.para_dict['d']) * self.para_dict['dt']
                if self.para_dict['n'] < 0.01:
                    self.para_dict['n'] = 0.01

                self.para_dict['a'] = self.para_dict['a'] + self.para_dict['dA'] * self.para_dict['dt']
                if self.para_dict['a'] < 1:
                    self.para_dict['a'] = 1

                self.para_dict['gdp'] = self.para_dict['k3']*self.para_dict['r']*self.para_dict['f']*self.para_dict['n']*self.para_dict['a']+self.para_dict['k4']*self.para_dict['r']*self.para_dict['a']
                self.para_dict['t']= self.para_dict['t']+self.para_dict['dt']

                # scale a and gdp for second axis
                tempa= self.para_dict['a']*8
                tempgdp =self.para_dict['gdp']*.8

                values_to_append= [self.para_dict['t'],self.para_dict['n'],tempa,self.para_dict['f'],tempgdp]
                self.master_array[self.para_dict['counter']]= values_to_append
                self.para_dict['counter'] += 1
            print("end loop")


    def graph_model(self):
        print("graph model enter")
        self.run_model()
        
        #split apart master array into temp arrays to make plot
        time_array = self.master_array[:,0]
        population_array = self.master_array[:,1]
        assets_array = self.master_array[:,2]
        nonrenewables_array = self.master_array[:,3]
        gdp_array = self.master_array[:,4]

        fig, ax1 = plt.subplots()

        # plot non-renewables
        color = "y"
        ax1.set_xlabel("time (years)")
        ax1.set_ylabel("F-NonRenewables & Assets")
        plt.xticks(np.arange(1850,2400,50)) # set x axis tick frequency
        lns1 = ax1.plot(self.master_array[:,0], nonrenewables_array, color=color, label="F-Nonrenewables")


        # plot assets
        color = "r"
        lns2 = ax1.plot(time_array, assets_array, color=color, label = "Assets")

        #make second axis for GDP and population that shares x-axis
        ax2 = ax1.twinx()

        #plot population
        color = "tab:pink"
        ax2.set_ylabel("Population & GDP")
        lns3 = ax2.plot(time_array, population_array, color=color, label="Population")
        
        #plot GDP
        color = "tab:blue"
        lns4 = ax2.plot(time_array, gdp_array, color=color, label="GDP")
        
        # add legend for 4 lines
        lns = lns1+lns2+lns3+lns4
        labs = [l.get_label() for l in lns]
        ax1.legend(lns, labs, loc=0)

        self.para_dict = copy.deepcopy(self.para_dict_reference) # reset parameters to initial value
        print("graph model end")
        print("print fig object", fig)
        
        return fig
    



            
         

test= EmergyModel()
print("about to call graph method")
test.graph_model()
print("end of script")
