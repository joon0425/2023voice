import h5py
import numpy
import scipy.io
import argparse
import os

cd = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

file = cd+"\\CREPE\\CREPENetfull.mat"
data = {}

"""
if file.endswith('.h5'):
    with h5py.File(file) as fd:
        for i in fd.keys():
            data[i] = fd[i][...]
    scipy.io.savemat(file[:-3] + '.mat', data)
elif file.endswith('.mat'):
    data = scipy.io.loadmat(file)
    print(data['__function_workspace__'])
    with h5py.File(file[:-4] + '.h5', 'w') as fd:
        for i in data.keys():
            if i not in ['__globals__',  '__header__', '__version__']:
                print(data[i])
                fd[i] = numpy.squeeze(data[i])
else:
    raise ValueError('filename must ends with .h5 or .mat')
"""

f = h5py.File(file)
print(f)