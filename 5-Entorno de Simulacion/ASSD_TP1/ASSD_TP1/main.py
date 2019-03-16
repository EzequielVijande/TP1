import GUI as g
import Manager as M
import UserData as u


interfaz = g.SimGUI()
data= u.UserData()
Controller= M.Manager(interfaz,data)

while ( (Controller.getState()) != M.EXIT):
    interfaz.Update()
    Controller.Dispatch(interfaz.GetEvent())


