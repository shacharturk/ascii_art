import re
import random
from typing import List


# all of the functions would get an open text file and return an open text file


def find_max(lines):
    maximum = 0
    for x in lines:
        if len(x) > maximum:
            maximum = len(x)
    return maximum


def rotate(text, angle):
    def mirror(file_name):
        txt = open(file_name, "r")
        lines = list(txt.readlines())
        maximum = find_max(lines)
        txt.close()
        txt = open(file_name, "w")
        for i in lines:
            a = i[:len(i)-2] #i needed to remove the line break and than return it for it to work
            txt.write((maximum-len(a))*" " + a[::-1]+chr(10))
        txt.close()


    def rotation(file_name):  # text is the file's name, because we need it to both read and write in it
        txt = open(file_name, "r")
        lines = txt.readlines()
        txt.close()
        result = open("temporal.txt", "w")
        maximum = find_max(lines)
        rev = list(reversed(lines))
        rev = rev[1:] #i needed to remove the line break here too, and here it was at the beginning
        for j in range(0, maximum - 1):
            line = ""
            for i in rev:
                if j < len(i):
                    line += i[j]
                else:
                    line += " "
            result.write(line + chr(10))
        result.close()
        read = open("temporal.txt", "r")
        r = read.readlines()
        txt = open(file_name, "w")
        for i in r:
            txt.write(i)
        read.close()
        txt.close()

    if angle != 360:
        for x in range(int(angle / 90)):
            rotation(text)
    else:
        mirror(text)


def convert(file_name, table, conversion_index):
    if conversion_index != 0:
        file = open(file_name, "r")
        txt = file.readlines()
        file.close()
        temp, line = [], ""
        for x in txt:
            for y in x:
                if ord(y) == 10:
                    line += chr(10)
                elif y == " ":
                    line += " "
                elif y in table:
                    line += table[y][conversion_index - 1]
                else:
                    line += "x"
            temp += line
            line = ""
        result = open(file_name, "w")
        for x in temp:
            result.write(x)
        result.close()


def serialize(file_name):
    a = open("outcome.txt", "a")
    a.close()
    result = open("outcome.txt", "w")
    txt = open(file_name, "r")
    lines: list[str] = txt.readlines()
    txt.close()
    for x in lines:
        line, last = "", x[0]
        count, i = 0, 0
        # checking the nuber of identical characters in a row:
        while i < len(x)-1:
            if x[i] == last:
                count += 1
            # adding the final number with the character to the serialized string
            if x[i] != last or i == len(x) - 1:
                line += str(count)
                line += last
                count = 1
            last = x[i]
            i += 1
        result.write(line)
        result.write(chr(10))


def deserialize(file_name):
    text = open(file_name, "r")
    lines = list(text.readlines())
    text.close()
    result = open("outcome.txt", "w")
    for x in lines:
        x = re.split('(\D)', x)
        i = 0
        line = ""
        while x[i] != "":
            count = 0
            while count < int(x[i]):
                line += x[i + 1]
                count += 1
            i += 2
        result.write(line)
        result.write(chr(10))
        print("line: " + line)
    result.close()

#I didn't find any conversion table with the instructions, so I had to generate one
table = {"#" : ("(", "e"), "!" : ("G", "W"), "$" : ("G", "L"), "%" : ("b", "8"), "&" : ("p", "p"), "'" : ("Z", "8"), "(" : ("}", "z"), ")" : ("c", "n"), "*" : ("[", "*"), "+" : ("*", "_"), "," : ("+", "Q"), "-" : ("W", "~"), "." : ("E", "M"), "/" : ("L", "1"), ":" : ("$", ":"), ";" : ("z", "*"), " < " : ("!", ")"), "= " : (" ^ ", "."), " > " : (".", "H"), "?" : ("{", "P"), " @ " : ("e", "v"), "A" : ("a", "o"), "B" : (": ", "O"), "C" : ("N", ", "), "D" : ("3", "v"), "E" : (";", "["), "F" : ("X", "t"), "G" : (" & ", "!"), "H" : ("5", " & "), "I" : ("r", "w"), "J" : ("8", "k"), "K" : ("q", "]"), "L" : ("n", "H"), "M" : ("$", "B"), "N" : ("8", "a"), "O" : ("}", " < "), "P" : ("Z", "]"), "Q" : ("X", "0"), "R" : ("z", " ^ "), "S" : ("x", "c"), "T" : (" * ", "?"), "U" : ("H", "]"), "V" : ("{", " > "), "W" : ("M", " * "), "X" : ("`", "v"), "Y" : ("0", "6"), "Z" : ("c", "`"), "[" : ("D", "S"), "^" : ("k", ";"), "]" : ("(", "T"), " ^ " : ("G", "p"), "_" : ("5", "x"), "`" : ("b", "b"), "a" : (" & ", "w"), "b" : ("M", "s"), "c" : ("T", "I"), "d" : ("X", "w"), "e" : ("= ", "_"), "f" : ("b", "6"), "g" : ("c", " % "), "h" : ("L", "f"), "i" : (" + ", "`"), "j" : ("p", "X"), "k" : ("8", "x"), "l" : ("Q", "e"), "m" : ("S", "o"), "n" : ("P", "~"), "o" : ("?", "N"), "p" : ("!", "7"), "q" : ("@", "j"), "r" : ("Q", "i"), "s" : ("C", "r"), "t" : ("J", "Z"), "u" : ("#", "."), "v" : (":", "k"), "w" : ("[", "5"), "x" : ("D", "="), "y" : ("/", ":"), "z" : ("S", "S"), "{" : ("}", "c"), "|" : ("L", "p"), "}" : ("%", "7")}


action = str(input("would you like to serialize or deserialize (or none)?"))
if action != "serialize" and action != "deserialize" and action != "none":
    raise Exception('illegal input: inexisting action')
file_name = str(input("on which file would you like this action to be performed?"))
if file_name[len(file_name)-4:] != ".txt":
    raise Exception('illegal input: illegal file name')
angle = int(input("at what angle would you like to rotate your picture?"))
if angle != 0 and angle != 90 and angle != 180 and angle != 270 and angle != 360:
    raise Exception('illegal input: only angles allowed are 0, 90, 180, 270, 360')
conversion = int(input("would you like to convert the chars in your picture? (0,1,2)"))
if conversion != 0 and conversion != 1 and conversion != 2:
    raise Exception('illegal input: conversion nuber can only be 1, 2, 3')

if action == "serialize":
    serialize(file_name)
elif action == "deserialize":
    deserialize(file_name)
else:
    txt=open(file_name,"r")
    lines = txt.readlines()
    txt.close()
    result=open("outcome.txt","w")
    for x in lines:
        result.write(x)
    result.close()
rotate("outcome.txt", angle)

convert("outcome.txt", table, conversion)
print('the file name is "outcome.txt"')
result = open("outcome.txt", "r")
lines = result.readlines()
result.close()
for i in lines:
    print(i[:len(i)-2])



