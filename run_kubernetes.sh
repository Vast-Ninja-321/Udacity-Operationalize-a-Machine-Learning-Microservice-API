#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=diegolythgoe/udacitymlservice

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run udacitymlservice \
	--image=$dockerpath \
	--port=80
# Step 3:
# List kubernetes pods
kubectl wait --for=condition=ready pod/udacitymlservice --timeout=120s
kubectl get pods

# Step 4:
# Forward the container port to a host

kubectl port-forward pod/udacitymlservice 8000:80 