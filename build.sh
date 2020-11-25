
docker build --tag adludiodev/example_cicd_docker_flask:1 .


docker run  -p 8890:80 -it adludiodev/example_cicd_docker_flask:1
