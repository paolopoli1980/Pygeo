##################################################################################
###################### Elliptic 2D bouncing ####################################
################################################################################


import math
import numpy
import matplotlib.pyplot as plt



xp=0
yp=10.1
puntix=[0]
puntiy=[10.1]
x0=1.4
y0=-9.6

puntix=[]
puntiy=[]

conta=0
xd=x0
yd=y0
t=0
tol=0.000001
conta=0
bounce=0

def disegna():
	plt.rc('xtick', labelsize=8)
	plt.rc('ytick', labelsize=8)
	plt.figure(figsize=(4, 8))
	plt.plot(puntix, puntiy)
	plt.title("test")
	plt.savefig("example.png")	
	plt.show()

 




def calcolo(x0,y0,xp,yp):
	global xnew
	global ynew
	uxperpend=-x0/(math.sqrt(x0**2+y0**2/16))
	uyperpend=-0.25*y0/math.sqrt((x0**2+y0**2/16))
	teta=math.pi
	uincx=(xp-x0)/math.sqrt((xp-x0)**2+(yp-y0)**2)
	uincy=(yp-y0)/math.sqrt((xp-x0)**2+(yp-y0)**2)
	matrixrot=[uxperpend**2+(1-uxperpend**2)*math.cos(teta), (1-math.cos(teta))*uxperpend*uyperpend,0],[(1-math.cos(teta))*uyperpend*uxperpend,uyperpend**2+(1-uyperpend**2)*math.cos(teta),0]
	xnew=matrixrot[0][0]*uincx+matrixrot[0][1]*uincy
	ynew=matrixrot[1][0]*uincx+matrixrot[1][1]*uincy
		 
 

while 1==1:
	calcolo(x0,y0,xp,yp)
 	conta+=1	
	if (conta%1==0):
		puntix.append(xd)
		puntiy.append(yd)
	t=(-(8*xnew*x0+2*ynew*y0)+math.sqrt((8*xnew*x0+2*y0*ynew)**2-4*(4*xnew**2+ynew**2)*(4*x0**2-100+y0**2)))/(2*(4*xnew**2+ynew**2))
 	xd=x0+t*xnew
	yd=y0+ynew*t	
	bounce+=1
 	xp=x0
	yp=y0
	x0=xd
	y0=yd
 		
 		
	if (-0.01<=xd<=0.01 and math.sqrt(100-4*xd**2)<=yd<=math.sqrt(100+4*xd**2)):
		disegna()
	
		break
		
					
 
