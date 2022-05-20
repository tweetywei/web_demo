# web_demo
This is a simple course feedback system. 
The main functions of this web site are:
  (1) Check course list 
  (2) fill out a feedback form for the course
  (3) Check the statistics chart of course ranking / grade distribution.


# HOW TO BUILD
```
docker build -t web_demo .
```
# HOW TO RUN
```
docker run -d --name web_demo_con -p 8000:8000 web_demo
```
Then you could access the website at 127.0.0.1:8000/dashboard/courses


