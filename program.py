import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

n = 2
x = [5, -60]
y = [15, 40]
m = [140, 150]
ax = 0
ay = 0
vx = 0
vy = 0
g  = 1
v  = 4
xz = -40
yz = 50
fi = 3.14/4
dt = 0.01
fimem = []
minmem = []
xp = []
yp = []
vx = np.cos(fi)*v
vy = np.sin(fi)*v
xp.append(1)
yp.append(1)
trenmin = 1000
xtm = []
ytm = []

for k in range(0, 200):
	ax = 0
	ay = 0
	vx = 0
	vy = 0
	g  = 1
	v  = 4
	fi = k*3.14/100
	dt = 0.01
	fimem.append(fi)
	xp = []
	yp = []
	vx = np.cos(fi)*v
	vy = np.sin(fi)*v
	xp.append(1)
	yp.append(1)
	min = ((xp[0]-xz)**2+(yp[0]-yz)**2)**0.5
	for i in range(0, 9000):
		for j in range(0, n):
			ax-=g*m[j]*(xp[i]-x[j])/((x[j]-xp[i])**2+(y[j]-yp[i])**2)**1.5
			ay-=g*m[j]*(yp[i]-y[j])/((x[j]-xp[i])**2+(y[j]-yp[i])**2)**1.5
		vx = vx+ax*dt
		vy = vy+ay*dt
		if(((xp[i]-xz)**2+(yp[i]-yz)**2)**0.5<min):
			min = ((xp[i]-xz)**2+(yp[i]-yz)**2)**0.5
		xp.append(xp[i]+vx*dt)
		yp.append(yp[i]+vy*dt)
		ax = 0
		ay = 0
	minmem.append(min)
	
	
ax = 0
ay = 0
vx = 0
vy = 0
g  = 1
v  = 4
for i in range(200):
	if(minmem[i] == np.min(minmem)):
		fi = i*3.14/100
xp = []
yp = []
vx = np.cos(fi)*v
vy = np.sin(fi)*v
xp.append(1)
yp.append(1)
for i in range(0, 9000):
	for j in range(0, n):
		ax-=g*m[j]*(xp[i]-x[j])/((x[j]-xp[i])**2+(y[j]-yp[i])**2)**1.5
		ay-=g*m[j]*(yp[i]-y[j])/((x[j]-xp[i])**2+(y[j]-yp[i])**2)**1.5
	vx = vx+ax*dt
	vy = vy+ay*dt
	xtm.append(xp[i]+vx*dt)
	ytm.append(yp[i]+vy*dt)
	xp.append(xp[i]+vx*dt)
	yp.append(yp[i]+vy*dt)
	ax = 0
	ay = 0
plt.figure(1)
plt.plot(xp, yp, 'r-')
plt.scatter(x, y)
plt.figure(2)
plt.plot(fimem, minmem)
plt.figure(3)
plt.plot(xtm, ytm, 'r-')
plt.scatter(x, y)
plt.scatter(xz, yz)
plt.show()