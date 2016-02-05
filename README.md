# EZregex

**[Cura](https://ultimaker.com/en/products/cura-software) search and replace plugin**

This rudimentary plugin allow you to substitute up to five differents regex per line of Gcode.
No need to rely on external editors before printing.

![Screenshot](https://github.com/theoo/EZregex/blob/master/img/screenshot.png)

## How to install

**linux** copy ezregex.py in __$USER/.cura/plugins/__ folder.

**other** [ultimaker wiki](http://wiki.ultimaker.com/How_to_use_plugins)

## How to use

Provide at least one search string and one replace string for the magic to happen.
Checkout [wikipedia definition of Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression) to learn how to write a regex.

## Why did I write this plugin

Because when switching tool on my printer its head can tilt to prevent material from mixing.
Unfortunately my firmware (smoothie) doesn't allow any sort of callback or further definition of the tool change command (Tn). Therefore I have to add some code around the Tn command to tilt the head, so easy with a regex ! And it's working like a charm.
