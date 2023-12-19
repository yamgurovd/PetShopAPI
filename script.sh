#!/bin/bash

docker-compose up --abort-on-container-exit
allure serve test_results
# wai for 2 seconds
sleep 2
docker-compose down --rmi allure
rm -rf test_results
mkdir test_results
sleep 2

echo "Docker-compose was run? allure was made, all containers and images deleted"