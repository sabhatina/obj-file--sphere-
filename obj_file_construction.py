import numpy as np
from numpy import linalg as LA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

N=[0.3,0.5,0] #unit vector of the plane
D=0.5
rho=D/LA.norm(N,2)
if(rho>1):
    exit(0)
center=rho*(N/LA.norm(N,2))

radius=np.sqrt(1-rho**2)
print(center)
print(rho)

verts=np.loadtxt('verts2.txt')
faces=np.loadtxt('faces2.txt')
normals=np.loadtxt('norms2.txt')
normals=-normals
c=0
x=[]
y=[]
z=[]
vert_index=[]

new_verts=[]
vert_delete=[]
for i in range(len(verts)):

    if (verts[i,0]>center[0]):# and verts[i,1]>center[1]):# and verts[i,2]>center[2]):#and verts[i,1]>center[1]
        new_verts.append(verts[i])
        x.append(verts[i,0])
        y.append(verts[i,1])
        z.append(verts[i, 2])
        vert_index.append(i)

    else:
        vert_delete.append(i)

row_to_delete=[]
print(len(new_verts))
print(len(faces))
for i in range(len(faces)):

    for j in vert_delete:
        if (faces[i][0] == j or faces[i][1] == j or faces[i][2] == j):

            row_to_delete.append(i)


mylist = list(dict.fromkeys(row_to_delete))
print(len(mylist))
new_faces = np.delete(faces, mylist, axis=0)
new_normals=np.delete(normals, mylist, axis=0)
print(len(new_faces))


thefile = open('test.obj', 'w')
for item in verts:
  thefile.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in new_normals:
  thefile.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in new_faces:
  thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0],item[1],item[2]))
thefile.write("\n")
with open('origin.txt', 'r') as File:
      info=File.readlines()
      for line in info:
          thefile.write(line)

thefile.write('\n')
thefile.write("f {0}//{3} {1}//{3} {2}//{3} \n".format(len(verts)+1,len(verts)+2,len(verts)+3,len(new_normals)+1))
thefile.write("f {0}//{3} {1}//{3} {2}//{3} \n".format(len(verts)+1,len(verts)+4,len(verts)+2,len(new_normals)+1))
thefile.close()
File.close()
