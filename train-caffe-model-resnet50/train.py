#coding=utf-8

import caffe
caffe.set_mode_gpu()
caffe.set_device(2)

solver = caffe.SGDSolver('/home/*/solver.prototxt')
solver.solve()
