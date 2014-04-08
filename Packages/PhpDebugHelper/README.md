## PhpDebugHelper

## Why?
This plugin help you when you are debugging your script. It frees you from writing so much function call such as `var_dump($var)` or `print_r($var)`. And you also can quickly clear all the debugging function calls.

## Where?
    https://github.com/yangxikun/sublime-phpdebughelper

## How?
+ Place cursor to a variable or index or property. If there are not variable be selected, it will still show the debugging function call.
+ Press **F1** or **F2**
+ Press **shift+f3** to navigate between debugging function calls
+ Press **F3** to clear

## Custom?
Save your our setting in `Preferences > Package Settings > PHP Debug Helper > Key Bindings-User` refer to the following:
~~~
[
    { "keys": ["f1"], "command": "php_debug_helper", "args": {"cmd": "prepend", "function": "var_dump"} },
    { "keys": ["f2"], "command": "php_debug_helper", "args": {"cmd": "append", "function": "var_dump"} },
    { "keys": ["f3"], "command": "php_debug_helper", "args": {"cmd": "clear", "function": ["var_dump"]} },
    { "keys": ["shift+f3"], "command": "php_debug_helper", "args": {"cmd": "show", "function": ["var_dump"]} }
]
~~~

You can change the function name that you use to debug and keymap. And you also can add more function here, for example(add `print_r`):
~~~
[
    { "keys": ["f1"], "command": "php_debug_helper", "args": {"cmd": "prepend", "function": "var_dump"} },
    { "keys": ["f2"], "command": "php_debug_helper", "args": {"cmd": "append", "function": "var_dump"} },
    { "keys": ["f4"], "command": "php_debug_helper", "args": {"cmd": "append", "function": "print_r"} },
    { "keys": ["f3"], "command": "php_debug_helper", "args": {"cmd": "clear", "function": ["var_dump", "print_r"]} },
    { "keys": ["shift+f3"], "command": "php_debug_helper", "args": {"cmd": "show", "function": ["var_dump", "print_r"]} }
]
~~~

## Improve

If you have any suggestion for this plugin, please make a issue.

## OK, Let's debug