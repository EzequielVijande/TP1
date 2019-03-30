import TransferCalculator as t
import UserData as u
import matplotlib.pyplot as plt
import numpy as np


data= u.UserData(f0=1000,fc=2000,f_sample=20000,DC=5)
calc= t.TransferCalculator()
calc.CalculateInputInTime(data)
calc.CalculateFAA_InTime(data)
calc.CalculateSH_InTime(data)
calc.CalculateAnalogKeyInTime(data)
calc.CalculateOutputInTime(data)
plt.plot(data.t, data.Output)
plt.show()
