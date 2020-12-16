# RClone


```python
#Mounting a remote as a local directory
!sudo mkdir /mnt/tmp
!rclone mount remote:/path/to/files /mnt/tmp
!fusermount -u /mnt/tmp
```


```python
#Syncing a remote with a local directory
!rclone sync source:path dest:path [flags]
#Example
!rclone sync /path/to/files ucbox:/ --create-empty-src-dirs
```

# Docker


```python
#Listing docker images
!docker images 
#List docker containers
!docker ps -a
#Removing all docker images
!docker rmi $(docker images)
#Removing all docker containers 
!docker rm $(docker ps -a)
#Running a docker container 
!docker run -i -t NAME /bin/bash
#Exporting a docker container to .tar archive
!docker export -o ~/Desktop/test.tar test
#Import an archived docker container as an image (an imported container == image)
!docker import ~/Desktop/test.tar
```
