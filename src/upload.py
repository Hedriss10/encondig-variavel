import os
import sys 

sys.path.append('..')


def db_request():
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data = os.path.join(file , 'data')
    csv = os.path.join(data, 'dataset.csv')
    
    return csv 
    
    
