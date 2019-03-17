import TransferCalculator as t
import UserData as u
import matplotlib.pyplot as plt


data= u.UserData(f0=10000,fc=50000)
calc= t.TransferCalculator()
calc.CalculateInputInTime(data)
calc.CalculateFAA_InTime(data)
plt.plot(data.t, data.FAA)
plt.show()
