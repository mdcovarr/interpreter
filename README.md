# interpreter
Writing a simple C language interpreter. Final project for course
CSE210A: Programming Languages at University of California,
Santa Cruz.


## Clone Repository
```
    git clone https://github.com/mdcovarr/interpreter.git
```


## Dependencies
* Parsing was done through the help of PyCParser.
* Python >= 3.7


## Script Help
Help on utilizing **__main__.py** script by running the following
command:
```
python __main__.py -h
```

You should be presented with the following output

```
usage: __main__.py [-h] [-f FILE]

Project to interpret a .c file

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  .c file to read in and interpret
```


## Usage
Pass in a **.c** file in order to be interpreted. For Example:
```
$ python __main__.py -f test.c
```

this will trigger the creation of an AST for file test.c. Followed
by interpretation of the AST, and execution of the **main** function.

