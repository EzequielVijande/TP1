import TransferCalculator as t
import UserData as u
import matplotlib.pyplot as plt
import numpy as np


data= u.UserData(f0=100,fc=5000,f_sample=2000,DC=5)
calc= t.TransferCalculator()
calc.CalculateInputInTime(data)
calc.CalculateFAA_InTime(data)
calc.CalculateSH_InTime(data)
plt.plot(data.t, data.SH)
plt.show()
