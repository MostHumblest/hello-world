import pandas as pd
import numpy as np
from pybaseball import batting_stats

START = 2001
END = 2002

batting =batting_stats(START, END, qual=200)
batting