# Tasks
All the tasks are done. 

### Task 1
  Project was Dockerized

### Task 2
 I used Alpine to scale the project. 

### Task 3
 Sentry, Elasticsearch, Logstash, and Kibana. The logs that are generated will be routed through Logstash and indexed in Elasticsearch, where you can visualize and analyze them using Kibana.

## Additional tasks 

Provided two docker-compose.yml files

It shows every errors and logs

The file mini-hacking.py, imitates the how the hacker could put the illegel items to the cart


# Installation

``sh
docker-compose up --build
``

It started the flask application and you can enter the project at 127.0.0.1:5000


``sh
docker-compose -f sentry-docker-compose.yml up