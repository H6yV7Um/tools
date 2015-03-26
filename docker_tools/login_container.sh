ip=`docker inspect 201a0a1fb0e9| grep IPAddress | awk -F'"' '{print $4;}'`
ssh root@$ip
