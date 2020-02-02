# Histy

Histy is a command line tool for generating histogram plots from timestamped logs.

Sample usage:
```bash
docker logs my-app --since "2020-01-06 12:37:30" --until "2020-01-06 12:38:30" | histy -b 10
```
