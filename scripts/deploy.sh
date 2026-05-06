export MINIKUBE_ROOTLESS=false
minikube start --driver=docker --container-runtime=docker
minikube addons enable registry
eval $(minikube -p minikube docker-env)

docker build -t valhalla-backend ./docker/backend
docker build -t valhalla-frontend ./docker/frontend
docker build -t valhalla-db ./docker/db

kubectl create ns valhalla

helm install valhalla ./charts/Valhalla -n valhalla