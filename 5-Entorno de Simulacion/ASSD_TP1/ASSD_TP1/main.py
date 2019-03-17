import GUI as g
import Manager as M
import TransferCalculator as t
import UserData as u


interfaz = g.SimGUI()
data= u.UserData()
calc= t.TransferCalculator()
Controller= M.Manager(interfaz,data,calc)

while ( (Controller.getState()) != M.EXIT):
    interfaz.Update()
    Controller.Dispatch(interfaz.GetEvent())


