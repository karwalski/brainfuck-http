# brainfuck-http
Challenging myself to build a python Brainfuck interpreter with ASCII control commands used to wrap HTTP.

Brainfuck is fun a 3-bit language, using just 8 characters as commands. Whilst it is Turing complete, it is mostly used to challenge programmers.

https://en.wikipedia.org/wiki/Brainfuck

## usage

Run `python3 bf.py test.bf`

The interpreter will process each valid brainfuck command character, with each of the bytes in the array populating at each step
```
Brainfuck Interpreter by Matthew Watt - Version 1.0 
File: test.bf 
 [0, 0] 
Pointer: 1 
Command 5 
Output: 
```

The test.bf brainfuck script outputs the ASCII characters 'Matt'
```
Brainfuck Interpreter by Matthew Watt - Version 1.0 
File: test.bf 
 [77, 97, 116, 116, 0] 


Output: Matt
```

## ASCII Control characters
The ASCII control characters are used to determine between HTTP headers and the request text.
http://jkorpela.fi/chars/c0.html

## Version
### 1.0
This release has a working interpretter of brainfuck, and was tested with a series of braindfuck scripts with limited complexity. Whilst it allows an unlimited depth of loops, and unlimited number of bytes - it was not designed for scalability and would likely hit python and system memory limitations at some point.
This version does not have any working HTTP functionality.
