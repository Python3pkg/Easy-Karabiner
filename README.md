#Easy-Karabiner
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

* Remap
* Definition
* Filter

Let me show you a simple example.

```python
# You must define all `Definition` in a dict named `DEFINITIONS`
# Otherwise Easy-Karabiner cannot find your `Definition`
DEFINITIONS = {
    # Define 'BILIBILI' as the name of 'com.typcn.Bilibili'
    # This is a application definition, and they have the form like
    #     'NAME': 'Identifier_Value'
    'BILIBILI': 'com.typcn.Bilibili',
    # You can find the 'Identifier_Value' by the follow steps:
    #   1. Open Karabiner preferences, find "Misc & Uninstall -> Launch EventViewer -> App"
    #   2. click the windows of the application you want to define
    #   3. copy the value in the "Application Bundle Identifier" column
}

REMAPS = [
    # Remap 'Left Ctrl'+'Tab' to 'Right Command'+'Right Option'+'Right' 
    # only when the active application is 'BILIBILI'
    #
    # So when you press 'Left Ctrl'+'Tab', the logic is:
    #
    #   if current_application == 'BILIBILI':
    #     return 'Right Command'+'Right Option'+'Right' 
    #   else:
    #     return 'Left Ctrl'+'Tab' 
    ['ctrl tab'      , 'cmd_r alt_r right', ['BILIBILI']],
    # This kind of `Remap` has the form like
    #     ['From_Key', 'Map_to_Key', ['Filter1', 'Filter2', ...]]
    ['ctrl shift tab', 'cmd_r alt_r left' , ['BILIBILI']],
]
```

##Remap
`Remap` is consist of four parts: `Remap_Type`, `From_Key`, `Map_to_Keys`, `Filters`. Only `From_Key` is required, others are optional.

```python
['(Remap_Type)', 'From_Key', 'Map_to_Key1', 'Map_to_Key2', ..., ['Filter1', 'Filter2', ...]]
```

The number of `Map_to_Key` could changed in different `Remap_Type`, but in most situations, there are only one or two `Map_to_Key`; and if you ignored `Remap_Type`, then only one `Map_to_Key` is allowed.

###Remap_Tyep
`Remap_Tyep` is used to tell Karabiner what kind of key-remapping it is. For example

```python
# Remapping double pressed 'fn' to 'F12'
# it keeps unchanged when single pressed 
['(double)', 'fn', 'F12'],
# Remapping double pressed 'brightness_up' to 'Open::COPY_FINDER_PATH' 
# and also remapping it to 'F2' 
['(double)', 'brightness_up', 'Open::COPY_FINDER_PATH', 'F2']
# Remapping 'esc' to 'cmd_r ctrl_r alt_r shift_r' when holding it
# it keeps unchanged when single pressed or other situations
['(holding)', 'esc', 'cmd_r ctrl_r alt_r shift_r']
```

###Key
`From_Key` and `Map_to_Key` has the same format, they are composed by space-separated key strings. Easy-Karabiner predefined some aliases for reducing tedious typing. You can found the predefined aliases [here](https://github.com/loggerhead/Easy-Karabiner/blob/master/easy_karabiner/alias.py).

###Filters
`Filters` is used to tell Karabiner when/where the key-remapping working or not working. For example

```python
# Remapping works only when current application is NOT 
# 'SKIM' or any applications defined in '{{EMACS_IGNORE_APP}}'
['ctrl P', 'up', ['!{{EMACS_IGNORE_APP}}', '!SKIM']]
# '!' before a filter means NOT, otherwise means ONLY
# Remapping works only when 'SKIM' or 'KINDLE'
['ctrl cmd F', 'cmd_r shift_r F cmd_r shift_r -', ['SKIM', 'KINDLE']]
```

To distinguish `Map_to_Keys` and `Filters`, you must use brackets or parentheses to tell Easy-Karabiner whether last part of a `Remap` is `Filters` or not.

##Definition
`Definition` is used to define `Filters` or specific `Key`, so you can use it in `Remap`. It has several forms

```python
DEFINITIONS = {
    # Define a filter or something else with name and value
    # `NAME` is a symbol to represent the ground-truth value which used in `REMAPS`
    'NAME': 'VALUE',
    # A `NAME` can represents multiple values
    'NAME': ['VALUE1', 'VALUE2', ...],
    # Same as above, except `DEF_TYPE` specified `Definition` type
    'DEF_TYPE::NAME': 'VALUE',
    'DEF_TYPE::NAME': ['VALUE1', 'VALUE2', ...],
}
```

NOTICE: only name part is used in `Filters`, so don't define two `Definition` with the same name.

For your convenience, there are some predefined `Definition` that you can direct used in `Filters`; and you can check it [here](https://github.com/loggerhead/Easy-Karabiner/tree/master/easy_karabiner/data/def).

###Replacement
A `NAME` enclosed with curly braces is a definition of `Replacement` filter.

```python
'{{NAME}}': ['VALUE1', 'VALUE2', ...]
```

`Replacement` filter will replaced by values defined in brackets.

###VKOpenURL
A `NAME` start with `Open::` is a definition of `VKOpenURL`, you can use it to open url, run application, or execute shell script.

```python
'Open::NAME': 'VALUE'
# Define a special key to represent opening an application
'Open::FINDER': 'Finder.app'
'Open::FINDER': '/Applications/Finder.app'
# open url
'Open::BAIDU': 'https://baidu.com'
# execute shell script
'Open::COPY_DATE': '#! /bin/date | /usr/bin/pbcopy'
# must start with `#! ` (there is a space!)
'Open::COPY_DATE': '''#! 
                      /bin/date | /usr/bin/pbcopy'''
```

NOTICE: `VKOpenURL` is used as a `Key` in `Remap` instead of `Filter`.

#LICENSE
MIT
