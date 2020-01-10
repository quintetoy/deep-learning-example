

#ubuntu16.04,cuda8.0安装caffe

```
apt-get update
sudo apt-get install git 
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libatlas-base-dev

sudo apt-get install python-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev

git clone http://github.com/bvlc/caffe.git
cd caffe/
mv Makefile.config.example Makefile.config

make clean
make all -j64

make pycaffe
export PYTHONPATH=......
echo 
```

```
opencv 安装路径/usr/local/lib
```

Q：

```
LD -o .build_release/lib/libcaffe.so.1.0.0-rc3
/usr/bin/ld: cannot find -lboost_python35
collect2: error: ld returned 1 exit status
Makefile:566: recipe for target '.build_release/lib/libcaffe.so.1.0.0-rc3' failed
make: *** [.build_release/lib/libcaffe.so.1.0.0-rc3] Error 1

```



A：

```
修改成这样，Makefile.config. PYTHON_LIBRARIES := boost_python-py35 python3.5m
```



Q

```
python/caffe/_caffe.cpp:10:31: fatal error: numpy/arrayobject.h: No such file or directory
```



```
/usr/local/lib/python3.5/dist-packages/numpy/core/include
```



Q: cd python  import caffe

```
ImportError: libopencv_core.so.3.4: cannot open shared object file: No such file or directory
```



把opencv的环境变量添加到bashrc中

```
export  LD_LIBRARY_PATH=/home/user/lib:$LD_LIBRARY_PATH
```



Q: ImportError: No module named 'google'

```
pip install protobuf -i https://pypi.tuna.tsinghua.edu.cn/simple
```



在相关的地方进行修改

<https://blog.csdn.net/chenhuan20123/article/details/79587773>

<https://blog.csdn.net/xunan003/article/details/79130493>

LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5 

在最后hdl5后面添加opencv_core opencv_highgui opencv_imgproc opencv_imgcodecs即可，变为

LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5 opencv_core opencv_highgui opencv_imgproc opencv_imgcodecs

然后重新编译。
--------------------- 
sudo gedit Makefile.config（对于只读文件的修改，这样也会更方面一些）
找到：
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib
修改为：
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
LIBRARY_DIRS := ​$(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial



[<https://www.twblogs.net/a/5be34baa2b717720b51d5eec/zh-cn>]

