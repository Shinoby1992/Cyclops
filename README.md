# Cyclops

A simple DOS attack tool

### Requirements
Python 3.*x*.*x*
<br>

**Attack a localhost on port 5000**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000
```

**Attack a localhost on port 5000 aggressive mode**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000 -m A
```

**Attack a localhost on port 5000 with 256 bots**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000 -t 256
```

**Attack a localhost on port 5000 with 256 bots aggressive mode**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000 -t 256 -m A
```

**Attack a localhost on port 5000 with 256 bots stealth mode**
```sh
$ python cyclops.py -i 127.0.0.1 -p 5000 -t 256 -m S
```
