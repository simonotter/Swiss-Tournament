# Read Me
This code base is my answer to the Tournament project in the [Udacity Introduction to Programming Nanodegree](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000).
## Installation
1. You need a machine running PostgreSQL and Python
2. Copy the **tornament** directory to your machine
3. From the command prompt, type:
```
$ cd <yourpath>/tornament
$ psql
=> \i tornament
```
This will establish the database, tables and views that the code requires.
## Running the Test Cases
To the run the test cases for this project provided by Udacity, type the following from a terminal on your machine (note: you will probably want to estabish a second terminal, so that you can keep the first one running in psql mode).
```
$ python tournament_test.py
```
## Licence
MIT License

Copyright (c) 2016 Simon Otter

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

