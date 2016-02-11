WIP
---
This project is a *work in progress*. The implementation is *incomplete* and
subject to change. The documentation can be inaccurate.

Avant Graph
===========

Avant graph is a program to visualize the collaboration of researchers at KTH.
The data set is taken from http://kth.diva-portal.org. If you are interested of
getting a copy of the database, send me a mail at henrye [at] kth [dot] se.

The name _Avant Graph_ is a play on words on the term _avant garde_.

Installation / Usage
--------------------

```shell
$ git clone git@github.com/karlek/avant-graph.git
$ cd avant-graph
$ python main.py
```

Dependencies
------------

* python-scipy
* python-cairo
* python-gobject
* python-graph-tool
* python-matplotlib

Flags
-----

* __-v/--verbose:__
	Enable debugging output.

Example
-------

This is a grouped version of a sfdp-layout.

![Original](https://github.com/karlek/avant-graph/blob/master/grouped.png?raw=true)

Public domain
-------------
I hereby release this code into the [public domain](https://creativecommons.org/publicdomain/zero/1.0/).
