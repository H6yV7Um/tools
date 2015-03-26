#! /bin/sh
# business install 
# script name : build.sh

#set -eu -o pipefail

VERSION="1.0.2"
FILE_NAME="aos-lh"
BUILD_NAME="./output"
CUR_DIR=`pwd`

echo "start building..."

find ./ -regex "\..+\.svn$" -type d | xargs rm -rf
if [ $? -ne 0 ]; then 
	echo "remove .svn dirs failed!"
	exit 1
fi

rm -rf $BUILD_NAME

objs=`ls .`

mkdir $BUILD_NAME
if [ $? -ne 0 ]; then 
	echo "create dir \"$BUILD_NAME\" failed!"
	exit 2
fi

mv $objs $BUILD_NAME/
if [ $? -ne 0 ]; then 
	echo "move files to dir \"$BUILD_NAME\" failed!"
	exit 3
fi

echo "\"$BUILD_NAME\" has been created at dir \"$CUR_DIR/output/\" successfully."
echo "building success!"
exit 0
