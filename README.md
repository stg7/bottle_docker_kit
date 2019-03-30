# docker-compose kit for python3 web apps with bottle
This docker-compose file is mainly based on the guide:

* https://github.com/tiangolo/uwsgi-nginx-docker

Both parts, the `docker-compose.yml` and `app/main.py` can be seen as a first starting point to develop a python3 web application.

## start

just run
```
docker-compose up -d web
```
and now your web-server is running at [http://localhost:8080](http://localhost:8080)

Defalult settings are performing python autoload, if the main.py is changed, for a production setup this should be changed (check `app/uwsgi.ini` and comment `py-autoreload = 2` line).


## example api runs
For a REST api check the main.py example, there is a small example provided, e.g.
```
curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:8080/api

```

should output:
```
{"request": {"key1": "value1", "key2": "value2"}}
```