#Easy-Karabiner
[![Travis Build Status](https://travis-ci.org/loggerhead/Easy-Karabiner.svg)](https://travis-ci.org/loggerhead/Easy-Karabiner)
[![Code Health](https://landscape.io/github/loggerhead/Easy-Karabiner/master/landscape.svg)](https://landscape.io/github/loggerhead/Easy-Karabiner/master)
[![Coverage Status](https://coveralls.io/repos/github/loggerhead/Easy-Karabiner/badge.svg)](https://coveralls.io/github/loggerhead/Easy-Karabiner)
[![PyPI version](https://img.shields.io/pypi/v/easy_karabiner.svg)](https://pypi.python.org/pypi/easy_karabiner)

[Karabiner](https://pqrs.org/osx/karabiner/index.html.en) is a great tool and I love it! But it's configuration is too complicated for newbies. For making life simpler, I have invented Easy-Karabiner, which is a tool to generate xml configuration for Karabiner from simple python script.

#Installation
```bash
pip install easy_karabiner
```

Or you can install manually

```bash
git clone https://github.com/loggerhead/Easy-Karabiner.git
cd Easy-Karabiner
python setup.py install
```

#Usage
Generate xml configuration from default path (`~/.easy_karabiner.py`), save it to `~/Library/Application Support/Karabiner/private.xml`, and reload Karabiner.

```bash
easy_karabiner
```

Same as above, except generating xml configuration from `./myconfig.py`.

```bash
easy_karabiner myconfig.py
```

Print generated xml configuration from a specific file.

```bash
easy_karabiner -s myconfig.py
```

See `easy_karabiner --help` for detailed options.

#How to write `~/.easy_karabiner.py`
Easy-Karabiner attempts to simplified the most commonly used configurations of Karabiner as well as possible, but there still exists some things you should know first. 

Or if you don't care about it and/or want to try it right now, [examples](https://github.com/loggerhead/Easy-Karabiner/tree/master/samples) are a good start :-)

##Basics
Karabiner is a context-aware key-remapping software, and Easy-Karabiner has simplified it's context and key-remapping to the combination of three components:

* Map
* Definition
* Filter

Let me show you a simple example.

```python
MAPS = [
    # Remap 1 press of 'Left Command'+'K' to 30 press of 'Up' 
    # only when the active application is 'Google Chrome'
	['cmd K', 'up '   * 30, ['Google Chrome']],
    ['cmd J', 'down ' * 30, ['Google Chrome']],
	# Swap 'Left Alt' to 'Left Command' only 
    # when the input keyborad is 'Cherry G80-3494'
    ['alt', 'cmd', ['CHERRY_GmbH_0011']],
    # You can get the peripheral name from `easy_karabiner -l` 
    ['cmd', 'alt', ['CHERRY_GmbH_0011']],
    # Press 'Left Alt'+'C' to open 'Google Chrome'
	['alt C', 'Google Chrome'],
]
```

In most simple situation, you don't need to define any thing, just write a `MAPS` by your intuition.

##Map

`Map` is consist of three parts: `Map_Command`, `KeyCombo`, `Filter`, none of these parts are necessary. 

```python
['_Map_Command_', 'KeyCombo1', 'KeyCombo2', ..., ['Filter1', 'Filter2', ...]]
```

The number of `KeyCombo` could be changed if  `Map_Command` changed, but in most situations, there are only one or two `KeyCombo`; and if you ignored `Map_Command`, then only two `KeyCombo` is allowed.

###Map_Command
`Map_Command` is used to tell Karabiner what kind of key-remapping it is. For example

```python
# Remapping double pressed 'fn' to 'F12'
# it keeps unchanged when single pressed 
['_double_', 'fn', 'F12'],
# Remapping 'esc' to 'cmd_r ctrl_r alt_r shift_r' when holding it
# it keeps unchanged when single pressed or other situations
['_holding_', 'esc', 'cmd_r ctrl_r alt_r shift_r']
```

Easy-Karabiner provide some aliases to help you remeber Karabiner `Map_Command`, include

| Alias            | Original              |
| ---------------- | --------------------- |
| `double`         | `DoublePressModifier` |
| `holding`        | `HoldingKeyToKey`     |
| `press_modifier` | `KeyOverlaidModifier` |

You can also use the original Karabiner `Map_Command`, For example

```python
# Reverse scroll direction if not Apple trackpad
['__FlipScrollWheel__', 'flipscrollwheel_vertical', ['!APPLE_COMPUTER', '!ANY']]
```

###KeyCombo

`KeyCombo` has the same format, they are composed by space-separated `Key`, and used to represent a combo of normal keys or actions. Easy-Karabiner predefined some aliases for reducing tedious typing. You can found the predefined aliases [here](https://github.com/loggerhead/Easy-Karabiner/blob/master/easy_karabiner/alias.py). 

Here is some example about `KeyCombo`

```python
# A single key
'alt'
# A shortcut 
'alt C'

# A special key-combo which represent one action--open application
'Google Chrome'

# A special key-combo which represent one action--exectue script 	
# script must start with '#! ' to tell Easy-Karabiner it's a script
'#! osascript /usr/local/bin/copy_finder_path'

# A special key-combo which represent two actions:
#   1. Click left mouse button
#   2. Execute script
# NOTICE: if a action contain space, you should use quote to tell
#         Easy-Karabiner that is a entirety.
'mouse_left "#! osascript /usr/local/bin/copy_finder_path"'
```

Because Easy-Karabiner verify a `Key` by check predefined XML file, but there exists some predefined `Key` not exists in any data file, so Easy-Karabiner will not prevent you to use a unknown `Key` but give you a warning. 

###Filter
`Filter` is used to tell Karabiner when/where the key-remapping working or not working. For example

```python
# Remapping works only when current application is NOT 
# 'Skim' or any applications defined in 'EMACS_IGNORE_APP' predefined replacement
['ctrl P', 'up', ['!EMACS_IGNORE_APP', '!Skim']]
# '!' before a filter means NOT, otherwise means ONLY
# NOTICE: How you define a thing, then how you use it in Easy-Karabiner.
#		  So, you don't need add '{{' and '}}' around a replacement.

# Remapping works only when 'Skim' or 'Kindle'
# NOTICE: You don't need to define a filter if it is application filter,
#		  Easy-Karabiner will do this job for you.
['ctrl cmd F', 'cmd_r shift_r F cmd_r shift_r -', ['Skim', 'Kindle']]
```

To distinguish `KeyCombo` and `Filter`, you must use brackets to tell Easy-Karabiner whether last part of a `Map` is a list of `Filter` or not. 

##Definition
`Definition` is used to define `Filter` or `Key`, so you can use it in `Map`. Because Easy-Karabiner auto-defined most things for you, so you don't need it in most situation. `Definition` has several forms

```python
DEFINITIONS = {
    # `NAME` is a symbol to represent the ground-truth value which used in `MAPS`
    'NAME': 'VALUE',
    # A `NAME` can represents multiple values
    'NAME': ['VALUE1', 'VALUE2', ...],
    # Same as above, except `DEF_TYPE` specified `Definition` type
    'DEF_TYPE::NAME': 'VALUE',
    'DEF_TYPE::NAME': ['VALUE1', 'VALUE2', ...],
}
```

The key of `Definition` is how you define it, how you use it; So you don't need to around a defined replacement with `{{` and `}}`.

For your convenience, Easy-Karabiner would use predefined `Definition`, so you don't need to define everything and just use it in `Filter`.

###Replacement
`Replacement` is a special `Definition` which will replaced by values when used. It has the form below

```python
'NAME': ['VALUE1', 'VALUE2', ...]
```

If Easy-Karabiner cannot guess `DEF_TYPE` from `VALUE`, then a `Definition` with above form will be defined as a `Replacement`. Easy-Karabiner will try to define any undefined values in `Replacement` to keep consistency with other parts, for example

```python
# Two keymap will be defined
'LAUNCHER_MODE_V2_EXTRA': [
    ['__KeyDownUpToKey__', 'C', 'Maps'],
    ['__KeyDownUpToKey__', 'V', 'FaceTime'],
]

# 'Sublime Text' and 'Visual Studio Code' will be defined
'emacs_ignore_app': [
    'ECLIPSE', 'EMACS', 'TERMINAL',
    'REMOTEDESKTOPCONNECTION', 'VI', 'X11',
    'VIRTUALMACHINE', 'TERMINAL', 'Sublime Text',
    'Visual Studio Code',
]
```

#LICENSE

MIT
