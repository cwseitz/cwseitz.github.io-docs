# Why I use Docker

I prefer to develop code on Ubuntu linux because of its relative simplicity but would rather not run Ubuntu as a primary OS because it doesn't support a number of applications like Microsoft Office, Adobe, etc. Also, I would prefer the "machine" (whatever that may mean) be local; worrying about a network connection, getting access to a server or hosting your own can be a headache. That being said, there are three main options: carry around two computers and upload everything to cloud storage, run a full-blown Ubuntu virtual machine with VirtualBox or other virtualization software or run a Ubuntu docker container. 

The first option is just plain impractical and inefficient. The virtual machine is nice because it has a GUI but can get pretty clunky because it is actually virtualizing hardware, using a kernel, and all of that typical operating system stuff. Docker, on the other hand, treats the OS more so as an *environment*. The OS and its configuration is available as an image and an instance of that image is called a *container* which you can run on a host operating system. You can have multiple containers based off of the original image all with different configurations for different purposes. In essence, Docker makes the OS portable: you can run Ubuntu native applications on any operating system with Docker installed and, if you are able to get access to a server, just install docker and create an instance of your local container on it with no repeated efforts. A containerized OS also means you can do whatever you want including deleting all system files - just create a new instance. Finally, a Docker container is just another isolated process on your host machine so computing resources shouldn't become an issue unless it already was.

Using Docker is not without issues, however. Docker images are usually stripped down versions of the actual OS meaning that that many of the utilities you would expect to come pre-installed, aren't. For the remainder of this brain-dump, I will write out a short tutorial on how to create a more usable image.

# Creating a docker image

After installing docker, you can see all of the images you have stored locally as follows:


```python
docker images 
```

Let's run the latest Ubuntu image on docker hub in interactive mode and mount the host Desktop to /mnt/tmp


```python
docker run -it -v /Users/cwseitz/Desktop:/mnt/tmp ubuntu /bin/bash
```

Now we have a bash shell inside the container and can run whatever commands we like to install necessary packages. I prefer to run a single bash script that installs everything I need:


```python
#!/bin/bash
echo "Building Ubuntu default image"
apt-get update
apt-get install -y git wget gcc vim
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
sha256sum Anaconda3-2020.07-Linux-x86_64.sh
bash Anaconda3-2020.07-Linux-x86_64.sh
source ~/.bashrc
eval "$(/root/anaconda3/bin/conda shell.bash hook)"
```


      File "<ipython-input-4-3f59cbde34e3>", line 2
        echo "Building Ubuntu default image"
             ^
    SyntaxError: invalid syntax



# Save the container as an image

First exit the container and check the containers you currently have. Find the name of the container you just constructed (in my case modest_agnesi) and run the following command to export it as a tar archive


```python
docker export modest_agnesi > ~/Desktop/modest_agnesi.tar
```

Finally if you want to import that image on this or another machine, run:


```python
docker import ~/Desktop/modest_agnesi.tar
```
