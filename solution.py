import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 530463349 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    t = 53
    len_x = len(x)
    loc = x.mean() - 1 / 2
    right_bound = 2/t**2 * (gamma(len_x).ppf(1 - alpha / 2)/len_x + loc) 
    left_bound = 2/t**2 * (gamma(len_x).ppf(alpha / 2)/len_x + loc) 
    return left_bound, right_bound
                            
