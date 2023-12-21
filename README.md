# Tasks
All the tasks are done. 

### Task 1
  Project was Dockerized

### Task 2
 Project is scaled up to 5 processes


### Task 3
 Sentry, Elasticsearch, Logstash, and Kibana. The logs that are generated will be routed through Logstash and indexed in Elasticsearch, where you can visualize and analyze them using Kibana.

## Additional tasks 

Provided two docker-compose.yml files

It shows every errors and logs

The file mini-hacking.py, imitates the how the hacker could put the illegel items to the cart


# Installation

```sh
docker build . -t ignitio 

docker stack deploy --compose-file=docker-compose.yml ignitio_web
```

It started the flask application and you can enter the project at 127.0.0.1:5000


```sh
docker-compose -f sentry-docker-compose.yml up --build
```

There are some migration issues with sentry so we need to migrate ourselves

```sh
docker container ps
```
Find your sentry container id and copy

```sh
docker exec -it "id" sentry upgrade 
```

After all there should be no issues.
If there are problems, promise I'll work on them.