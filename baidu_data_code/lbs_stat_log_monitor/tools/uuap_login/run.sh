

d=`date +%Y%m%d`
cat abc|sed -r "s/(.*s1\.pan\.bdstatic\.com.*\.(png|js|css))(\?r=[^&]*)*(.*)/\1\?r=$d\4/g"
