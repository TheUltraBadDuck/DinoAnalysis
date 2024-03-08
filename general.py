import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import boxcox



modify_funcs = [np.log, np.sqrt, np.cbrt,
                lambda x: np.log(x) ** 2, lambda x: boxcox(x)[0], lambda x: np.abs(x - np.mean(x))]

error_avoid_modify_funcs = [lambda x: np.log(x + 1), lambda x: np.sqrt(x + 1), np.cbrt,
                lambda x: np.log(x + 1) ** 2, lambda x: boxcox(x + 1)[0], lambda x: np.abs(x - np.mean(x))]

modify_names = ["Log", "Square root", "Cube root", "Log squared", "Boxcox", "Mean substract"]


def check_modifications(df: pd, feature: str, original_colour: str = "steelblue", modified_colour: str = "midnightblue", showing: bool = True):
    global modify_funcs
    global modify_names

    fig = plt.figure(layout=None, figsize=(12, 5))
    gs = fig.add_gridspec(nrows=2, ncols=5, hspace=0.3, wspace=0.3)

    ax_big = fig.add_subplot(gs[:, :2])
    ax_big.hist(df[feature], color=original_colour)
    ax_big.set_xlabel("Original", fontsize=12, fontweight="bold")
    
    for i in range(6):
        new_i = i + (i // 3) * 2 + 2
        ax = fig.add_subplot(gs[new_i // 5, new_i % 5])
        try:
            ax.hist(modify_funcs[i](df[feature]), color=modified_colour)
        except:
            ax.hist(error_avoid_modify_funcs[i](df[feature]), color=modified_colour)
            
        ax.set_xlabel(modify_names[i], fontsize=12, fontweight="bold")

    fig.suptitle(f"Modified feature [{feature}]", fontsize=18, fontweight="bold", y=0.95)
    if showing:
        plt.show()
        return None
    else:
        plt.close(fig)
        return fig