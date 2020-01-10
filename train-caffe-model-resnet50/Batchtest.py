#!/usr/bin/env
import sys
from PIL import Image,ImageDraw, ImageFont
import caffe
import numpy as np
import json
import os
import shutil
import importlib
importlib.reload(sys)


Testpicpath='/home/pic/'
savedir='/home/save'


root='/home/*/'   #根目录
deploy=root + '/ResNet-50-deploy.prototxt'    #deploy文件
caffe_model=root + 'caffecode/models/solver.caffemodel'   #训练好的 caffemodel

#打开查询的json表
json_dir='./sku-class.json'
class_sku_dict={}
with open(json_dir) as f:
    pop_data=json.load(f)
    for pop_dict in pop_data:
        class_sku_dict[pop_dict['class']]=pop_dict['sku']



net = caffe.Net(deploy,caffe_model,caffe.TEST)   #加载model和network

#图片预处理设置
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2,1,0))


#随机找的一张待测图片
file=[f for f in os.listdir(Testpicpath) if not f.startswith('.')]
num=0
for subdir in file:
    if os.path.splitext(subdir)[1]=='.jpg':
        img=os.path.join(Testpicpath,subdir)
        pic=Image.open(img).convert('RGB')
        im=caffe.io.load_image(img)                   #加载图片
        net.blobs['data'].data[...] = transformer.preprocess('data',im)      #执行上面设置的图片预处理操作，并将图片载入到blob中
        #执行测试
        out = net.forward()
        prob= net.blobs['prob'].data[0].flatten()
        print (prob)
        order=prob.argsort()[-1]  #将概率值排序，取出最大值所在的序号
        sku=class_sku_dict[int(order)]
        
        dir=savedir+'/'+str(sku)
        if dir and not os.path.exists(dir):
            os.makedirs(dir)

   
        save_path=dir+'/'+sku+'_'+subdir

        class_score=prob[order]

        pic.save(save_path)

