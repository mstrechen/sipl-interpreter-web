# sipl-interpreter-web

Simple web interface for **SIPL** interpreter.

This readme also avaliable on [ukrainian](README.ukr.md)


**SIPL** stands for **S**imple **I**mperative **P**rogramming **L**anguage.
It's simple programming language (obviously) used to explain Programming Theory on the example.
Learn more [here](http://csc.knu.ua/en/library/books/nikitchenko-7.pdf) (ukraininan). 


### How to run using docker

- Build docker image with `docker build -t sipl-web .`
- Run with `docker run -d --rm -p 80:8080 sipl-web`
- Now just go to `http://127.0.0.1` and use it! 

### Run interpreter without web interface

At the project root you could find `sipl-interpreter.jar` which could be used to interpret 
programs without running web interface. It has pretty easy CLI:
```
java -jar sipl-interpreter.jar 
 -e,--env-file <arg>   environment file path
 -p,--path <arg>       program file path
```

For example, run the program without any initial state of variables:

```shell script
java -jar sipl-interpeter.jar program.sipl 
# or 
java -jar sipl-interpeter.jar -p program.sipl
```

To add initial state of variables you could also use env file:
```shell script
java -jar sipl-interpeter.jar -e env.file -p program.sipl 
``` 

Note that env.file should have the following format:
```
<VARIABLE_1>=<VALUE_1>
...
<VARIABLE_N>=<VALUE_N>
```
e.g. 
```
A=1
B=2
```

Note that you should use *only* numbers to set values.
Spaces after and before the '=' is also unacceptable.

It's also possible to use other dict-like syntax, e.g.:
```
{A=1, B=2, C=3}
```
(However, spaces before and after '=' is still not allowed)

### How to try it in other way?

Currently, it's also hosted on UpCloud, so you can also try this out by following the [link](http://94-237-94-186.de-fra1.upcloud.host). 

Have fun!
