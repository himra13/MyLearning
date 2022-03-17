######################################################################
########################### MDE components ###########################
######################################################################
# MDE = z-score * pooled_standard_deviation
######################################################################
# z-score = z(1-alpha/2) + z(1-beta)
# alpha is probability of false positive rate
# beta is probability of catching the difference false negative
######################################################################
# pooled_standard_deviation depends on type of metric we are working on
# If it's mean, we can use weighted_average formula on size to calculate it.
# If it's proportion, we need to use another
######################################################################

import numpy as np
from typing import Optional
from scipy.stats import norm

def cal_zscore(alpha: Optional[float] = 0.45, beta: Optional[float] = 0.8):
    Z_alpha = abs(norm.ppf(1 - alpha))
    Z_beta = abs(norm.ppf(1 - beta))
    return Z_alpha + Z_beta

def cal_pooled_variance(a: np.array, b: np.array, metric_type: str = ['mean', 'proportion']):
    if metric_type == 'mean':
        if len(a) >= 30 & len(b) >= 30:
            pooled_variance = (len(a) * a.std() + len(b) * b.std()) / (len(a) + len(b))
            return pooled_variance
        else:
            pooled_variance = ((len(a) -1) * a.std() + (len(b) - 1) * b.std()) / (len(a) + len(b) - 2)
            return pooled_variance
    else:
        raise NameError('This option is not available.')

def cal_mde(a: np.array, b: np.array, metric_type: str = ['mean', 'proportion'], format: str = ['mde', 'mde_pct'], alpha: Optional[float] = 0.45, beta: Optional[float] = 0.8):
    """
    Cal MDE is formula to calculate Minimum detectable effect
    ====================================================================
    INPUT PARAMETERS
    ----------
    - 'a' is an array format of difference between prepre and pre period of experiment of A variant on metric for allocation
    - 'b' is an array format of difference between prepre and pre period of experiment of B variant on metric for allocation
    - 'metric_type' is type of calculation we want to compare
    - 'format' is output format we want to have, normally, I would suggest 'mde_pct' for the sake of simplicity.
    - 'alpha' is false positive rate, this identify P(False|True)
    - 'beta' is false negative rate, this identify power of getting it correct on Negative. P(False|False)
    --------------------------------------------------------------------
    OUTPUT
    ----------
    - mde: give a same unit as input a, b unit
    - mde_pct: use as an uplift percentage that treatment group should have
    """
    if metric_type == 'proportion':
        raise NameError('This option is not available.')
    
    mde = cal_zscore(alpha, beta) * cal_pooled_variance(a, b, metric_type = metric_type)

    if format == 'mde':
        return mde
    else:
        return mde/a.mean()

def old_mde_formula(avg: float, var: float, observation: int, alpha: Optional[float] = 0.05, beta: Optional[float] = 0.8):
    """
    Calculate MDE: 
    ------------------------------------------
    - normal alpha=0.05, beta=0.2
    - given that metric is average
    ------------------------------------------
    OUTPUT
    return MDE percentage
    """
    Z_alpha = abs(norm.ppf(1 - alpha))
    Z_beta = abs(norm.ppf(1 - beta))
#     return (Z_alpha,Z_beta)
    MDE = (Z_alpha + Z_beta) * np.sqrt( 4 * var / observation) / avg
    return MDE

# test code
if __name__ == '__main__':
    # help(cal_mde)
    print("haven't test code with real data")