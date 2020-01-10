#!/usr/bin/env sh
MY=/home/*/


echo "Create train lmdb.."
rm -rf $MY/img_train_lmdb
/opt/caffe/build/tools/convert_imageset \
--shuffle \
/home/*/ \
$MY/train.txt \
$MY/img_train_lmdb

echo "Create test lmdb.."
rm -rf $MY/img_test_lmdb
/opt/caffe/build/tools/convert_imageset \
--shuffle \
/home/*/ \
$MY/test.txt \
$MY/img_test_lmdb

echo "All Done.."
