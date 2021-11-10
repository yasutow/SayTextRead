# SayTextRead
## Description
This simple package produces the estimated time to finish reading a set of .txt files written in Japanese language.
For the default case, this program wraps the say command included in Mac OS.
Note that this program runs the subprocess.call with shell=True.

Alternatively, pyttsx3 could be used if use_say is set to False, which is still a test version.

## Requirements
Mac OS Big Sur 11.4
pyttsx3 == 2.90

## Install
```
$ cd SayTextRead
$ python setup.py develop
```

## Usage
```
>>> import SayTextRead
>>> SayTextRead.saytextread(["./in_1.txt"])
```
