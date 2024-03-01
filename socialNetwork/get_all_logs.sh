#!/bin/bash

# Define the directory to save logs
dir="data/logs"
mkdir -p $dir

# Get the list of all services in the docker-compose project
services=$(sudo docker-compose ps --services)
echo "Services: $services"

for service in $services; do
    echo "Collecting logs for $service"
    # Use docker-compose logs to get logs for each service
    sudo docker-compose logs $service > "$dir/$service.log"
done

echo "Logs collected in $dir"
