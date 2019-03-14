import GUI as g
import Manager as M


interfaz = g.SimGUI()
Controller= M.Manager(interfaz)
while ( (Controller.getState()) != M.EXIT):
    interfaz.Update()
    Controller.Dispatch(interfaz.GetEvent())


