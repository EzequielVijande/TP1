import TransferCalculator as t
import UserData as u
import matplotlib.pyplot as plt
import numpy as np


data= u.UserData(f0=10000,fc=200000,f_sample=400000,DC=5)
calc= t.TransferCalculator()
calc.CalculateInputInTime(data)
calc.CalculateFAA_InTime(data)
calc.CalculateSH_InTime(data)
calc.CalculateAnalogKeyInTime(data)
calc.CalculateOutputInTime(data)
plt.plot(data.t, data.SH)
plt.show()
