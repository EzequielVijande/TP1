import TransferCalculator as t
import UserData as u
import matplotlib.pyplot as plt
import numpy as np


data= u.UserData(f0=1000,fc=500)
calc= t.TransferCalculator()
calc.CalculateInputInTime(data)
calc.CalculateFAA_InTime(data)
plt.plot(data.t, data.FAA)
plt.show()
