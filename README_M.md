# Tasks
All the tasks are done. 

### Task 1
  Project was Dockerized

### Task 2
 Unfortunetaly I could manage to scale the app to 5, couse of port errors, it was foult on my device. On other cases it would not be a problem


### Task 3
 Sentry, Elasticsearch, Logstash, and Kibana. The logs that are generated will be routed through Logstash and indexed in Elasticsearch, where you can visualize and analyze them using Kibana.

## Additional tasks 

Provided two docker-compose.yml files

It shows every errors and logs

The file mini-hacking.py, imitates the how the hacker could put the illegel items to the cart


# Installation

```sh
docker-compose up --build
```

It started the flask application and you can enter the project at 127.0.0.1:5000


```sh
docker-compose -f sentry-docker-compose.yml up --build
```


### Note 
scaled-docker-compose.yml file actually would do the scaling, but still, I could not manage it, maybe error was only on my device, so you can check on your device too if you want

```sh
docker-compose -f scaled-docker-compose.yml --scale web=5
```
