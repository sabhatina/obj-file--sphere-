
from skimage import measure
import scipy.io

import numpy as np
import math
import scipy

import h5py
def sphere(shape, radius, position):

    semisizes = (radius,) * 3


    grid = [slice(-x0, dim - x0) for x0, dim in zip(position, shape)]
    position = np.ogrid[grid]

    arr = np.zeros(shape, dtype=float)
    for x_i, semisize in zip(position, semisizes):
        arr += (np.abs(x_i / semisize) ** 2)

    return arr <= 1.0
radius=10
arr = sphere((10, 10, 10), radius, (0, 0, 0))



angle=450

c=np.cos(angle)
s=-np.sin(angle)
rx=np.asarray([[1,0,0],[0,c,-s],[0,s,c]])
ry=np.asarray([[c,0,s],[0,1,0],[-s,0,c]])
rz=np.asarray([[c,-s,0],[s,c,0],[0,0,1]])

verts, faces, normals, values = measure.marching_cubes_lewiner(arr,None,(1,) * 3)

verts=np.dot(verts,ry)

verts[:,0]=-verts[:,0]
verts[:,2]=verts[:,2]+8
verts=verts*0.05
verts=verts+0.25

a=[]

faces=faces+1

normals=-normals

thefile = open('test.obj', 'w')
for item in verts:
  thefile.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in normals:
  thefile.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in faces:
  thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0],item[1],item[2]))
thefile.write("\n")
with open('origin.txt', 'r') as File:
      info=File.readlines()
      for line in info:
          thefile.write(line)

thefile.write('\n')
thefile.write("f {0}//{3} {1}//{3} {2}//{3} \n".format(len(verts)+1,len(verts)+2,len(verts)+3,len(normals)+1))
thefile.write("f {0}//{3} {1}//{3} {2}//{3} \n".format(len(verts)+1,len(verts)+4,len(verts)+2,len(normals)+1))
thefile.close()
File.close()