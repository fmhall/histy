<p align="center">
  <a href="https://github.com/bloXroute-Labs/bxgateway/blob/develop/LICENSE.md">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="histy is released under the MIT license." />
  </a>
  <a>
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs welcome!" />
  </a>
  <a href="https://badge.fury.io/py/histy">
    <img src="https://badge.fury.io/py/histy.svg" alt="PyPI version" height="18">
  </a>
  <a href="https://python.org">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.6%20%7C%203.7-blue">  
  </a>
</p>

# Histy

Histy is a command line tool for generating histogram plots from timestamped logs. 
Timestamps must be in ISO format.
Histy is useful for quick visual analysis of log frequencies from the command line

### Parameters:
`--bucket_time_s` or `-b` : the duration of each histogram bucket in seconds 

### Sample usage:
```bash
docker logs my-app --since "2020-01-06 12:37:30" --until "2020-01-06 12:38:30" | histy -b 10
```
```bash
cat server.log | histy -b 60
```