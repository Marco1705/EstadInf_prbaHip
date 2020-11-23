import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss
from scipy.special import ndtri
import datetime as dt

front = pd.read_csv('Border_Crossing_Entry_Data.csv')
is_tx = front["Port Name"] == "El Paso"
is_ped = front["Measure"] == "Pedestrians"
front["Date"] = pd.to_datetime(front["Date"], format="%m/%d/%Y")
is_year = front["Date"].dt.strftime("%Y").isin(["2000","2001","2002","2003","2004","2005","2006","2007","2008"])
is_year2 = front["Date"].dt.strftime("%Y").isin(["2000","2002","2004"])
is_2019 = front["Date"].dt.strftime("%Y") == "2019"
is_enero = front["Date"].dt.strftime("%m") == "01"
is_febrero = front["Date"].dt.strftime("%m") == "02"
is_marzo = front["Date"].dt.strftime("%m") == "03"

##Creacion de frames
frameene = front[is_tx & is_ped & is_year & is_febrero]
framefeb = front[is_tx & is_ped & is_year2 & is_febrero]
framemar = front[is_tx & is_ped & is_year & is_marzo]
frame1 = front[is_tx & is_ped & is_year & is_enero]
frame2 = front[is_tx & is_ped & is_2019 & is_marzo]
##print(frame2)
##MEDIA

mediamar = framemar.Value.mean()
mediafeb = framefeb.Value.mean()
media = frame1.Value.mean()

##DESVIACION ESTANDAR

desv_estand = frame1.Value.std()
desv_estand2 = framefeb.Value.std()
desv_estand3 = framemar.Value.std()
#print("Media Feb", mediafeb)
#print("Media Enero", media)
#print("Media Marzo", mediamar)
#print("Desv Est Enero", desv_estand)
#print("Desv Est Feb", desv_estand2)
#print("Desv Est Mar", desv_estand3)

##ESTANDARIZACION
estandar = (582606-media)/(desv_estand/3)
estandar2 = (382224-mediafeb)/(desv_estand2/3)
estandar3 = (643868-mediamar)/(desv_estand3/3)

#print("Valor para poner en funcion de la normal en enero", estandar)
#print("Valor para poner en funcion de la normal en febrero", estandar2)
#print("Valor para poner en funcion de la normal en marzo", estandar3)

##GRAFICA
#x1 = framefeb["Date"]
#y1 = framefeb["Value"]

#x1 = framemar["Date"]
#y1 = framemar["Value"]

x1 = frameene["Date"]
y1 = frameene["Value"]

plt.plot(x1,y1)
plt.show()

##funciones

normalen = ss.norm.cdf(-.131)
normalen1 = ndtri(.447)
normalfeb = ss.norm.cdf(-.199)
normalfeb2 = ndtri(.023)
normalmar = ss.norm.cdf(-.834)
normalmar2 = ndtri(.203)


#print("Final", normalen)
#print("Corroboracion", normalen1)
#print("Final", normalfeb)
#print("Corroboracion", normalfeb2)
#print("Final", normalmar)
#print("Corroboracion", normalmar2)
