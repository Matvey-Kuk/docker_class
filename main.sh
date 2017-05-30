##########################
# What is image
##########################

docker pull ghost

docker images

docker images -a

docker rmi ghost

##########################
# What is container
##########################

docker run ghost

docker run --name ghost-container -d ghost

docker run -d ghost

docker ps

docker ps -a

docker logs ghost-container

docker stop ghost-container

docker rm ghost-container

docker exec -it ghost-container bash

##########################
# Build first cute image
##########################

cd build_image_1;
docker build -t my_ghost .;
docker images;

# Todo: start
# https://store.docker.com/images/ghost - find images github and see difference between alpine and debian based images.
# Todo: end

# Todo: start
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/ Find difference between "RUN" & "CMD".
# Make image which prints "hello" + your name.
# Todo: end

# Todo: start
# Run your image, find your "hello" in logs.
# Todo: end

##########################
# Volumes
##########################

docker run --name ghost-container -v ~/Desktop/docker_meetup/connected_volume:/var/lib/ghost ghost

docker volume ls

docker inspect ghost-container

docker run --name ghost-container -v /var/lib/ghost ghost

##########################
# Port forwarding
##########################

docker run -p 8080:2368 --name ghost-container -d ghost

docker ps

# Todo: start
# Open localhost:8080. Click "Menu -> Home" link. Fix issue using volumes.
# Todo: end

# Todo: start
# Read https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#add-or-copy and build new my_docker image using "ADD" or "COPY".
# Start container without volumes and check if link works well.
# Todo: end

##########################
# Containers linking
##########################

docker network ls

docker run -itd --name=container1 busybox

docker run -itd --name=container2 busybox

docker network inspect bridge

docker attach container1

# Execute inside: ifconfig

docker network create --driver bridge my_network

docker run -itd --name=container1 --network=my_network busybox

docker run -itd --name=container2 --network=my_network busybox

docker attach container1

# Execute inside: ping container2

##########################
# Docker compose
##########################

docker-compose up

# Todo: start
# Run your my_ghost using this docker-compose
# Todo: end

##########################
# Cleanup
##########################

docker rm $(docker ps -a -q)

docker rmi $(docker images -q)

docker volume rm $(docker volume ls -qf dangling=true)
