# Cyclops

A simple DOS attack tool

### Requirements
Python 3.*x*.*x*
<br><br>
**Attack a localhost on port 5000**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000
```

**Attack a localhost on port 5000 aggressive mode**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000 -m A
```

**Attack a localhost on port 5000 with 4096 bots**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000 -t 4096
```

**Attack a localhost on port 5000 with 2048 bots arregessive mode**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000 -t 2048 -m A
```
