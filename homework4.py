import pylab as pl 
import math
v0=700
x0=0
y0=0
totaltime=20
timestep=0.1
m0=1
X1=[]
Y1=[]
for i in range(5):
	time=0
	x=0
	y=0
	v=v0
	X1.append(0)
	Y1.append(0)
	angle=(i+1)*5+30
	sinx=math.sin(angle*math.pi/180)
	cosx=math.cos(angle*math.pi/180)
	vx=v*cosx
	vy=v*sinx
	while y>=0:
		c=4e-5
		g=9.8
		d=6.5e-3
		a=(1- d*y/288)**2.5
		x=x+vx*timestep
		y=y+vy*timestep
		velocity=vx**2+vy**2
		v=math.sqrt(velocity)
		vx=vx-c*v*vx*timestep*a
		vy=vy-(c*v*vy*timestep*a)*abs(vy)/vy-g*timestep
		time+=timestep
		X1.append(x)
		Y1.append(y)
		if y<0:
			print(x)
		
	pl.plot(X1,Y1)
	pl.title('cannon shell including both air drag and the reduced air density at high altitudes')
	pl.xlabel('x ($m$)')
	pl.ylabel('y ($m$)')
	pl.ylim(0)
	pl.show()
