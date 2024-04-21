# Simple 'ls' utility using Python
A simple python program that prints the contents of an input json file to console in the style of 'ls' utility.


## Table of Contents

1. [Installation](#installation)
2. [Input JSON format](#input)
3. [Usage and Examples](#usage)


<a name="installation"></a>
## Installation

Only requirement for this program is presence of Python 3.x and pip.

Once Python 3 and pip are installed, simply run the following pip command:
```
pip install -i https://test.pypi.org/simple/ pyls-rehan
```


<a name="input"></a>
## Input JSON format
The input JSON file should be in the following format:
```
{
  "name": <str>,
  "size": <int>,
  "time_modified": <unix-timestamp>,
  "permissions": <string>,
  "contents": [
    {
         "name": ...,
         "size": ...,
         "time_modified": ...,
         "permissions": ...,
     },
     {
         "name": ...,
         "size": ...,
         "time_modified": ...,
         "permissions": ...
     },
     ...
     ...
     ...
    }
  ]
}
```
- Field 'name' refers to the name of the file or directory.
- Field 'size' refers to the size on disk in bytes.
- Field 'time_modified' refers to the time the file or directory was last modified in unix timestamp.
- Field 'permissions' refers to the permissions for the file or directory in unix terms.
- Field 'contents' is only present for directories and can contain a list of other items that are present within the directory.


<a name="usage"></a>
## Usage and Examples
Once installed, 'pyls' command can be used directly from the terminal.


- input_json_path : Path of input JSON file to be parsed (Required positional argument).
```
$  pyls ./input.json
LICENSE    README.md    ast    go.mod    lexer    main.go    parser    token  
```
- relative_path : Display only the contents of the relative path within the input JSON. (Optional second positional argument)
```
$  pyls ./input.json parser -l
Total 3
-rw-r--r-- 	 533 	 Nov 14 10:33 	 go.mod
-rw-r--r-- 	 1622 	 Nov 17 06:35 	 parser.go
-rw-r--r-- 	 1342 	 Nov 17 07:21 	 parser_test.go

$  pyls ./input.json parser/parser.go -l
Total 1
-rw-r--r-- 	 1622 	 Nov 17 06:35 	 parser.go
```
- -A, --all : Display all files and directories including hidden files starting with '.'
```
$  pyls ./input.json -A
.gitignore    LICENSE    README.md    ast    go.mod    lexer    main.go    parser    token  
```
- -l, --longformat : Display the results vertically with detailed information in long format.
```
$  pyls ./input.json -Al
Total 9
-rw-r--r-- 	 8911 	 Nov 14 05:57 	 .gitignore
-rw-r--r-- 	 1071 	 Nov 14 05:57 	 LICENSE
-rw-r--r-- 	 83 	 Nov 14 05:57 	 README.md
drwxr-xr-x 	 4096 	 Nov 14 10:28 	 ast
-rw-r--r-- 	 60 	 Nov 14 08:21 	 go.mod
drwxr-xr-x 	 4096 	 Nov 14 09:51 	 lexer
-rw-r--r-- 	 74 	 Nov 14 08:27 	 main.go
drwxr-xr-x 	 4096 	 Nov 17 07:21 	 parser
drwxr-xr-x 	 4096 	 Nov 14 09:27 	 token
```
- -r, --reverse : Display the results in reverse order.
```
$  pyls ./input.json -Alr
Total 9
drwxr-xr-x 	 4096 	 Nov 14 09:27 	 token
drwxr-xr-x 	 4096 	 Nov 17 07:21 	 parser
-rw-r--r-- 	 74 	 Nov 14 08:27 	 main.go
drwxr-xr-x 	 4096 	 Nov 14 09:51 	 lexer
-rw-r--r-- 	 60 	 Nov 14 08:21 	 go.mod
drwxr-xr-x 	 4096 	 Nov 14 10:28 	 ast
-rw-r--r-- 	 83 	 Nov 14 05:57 	 README.md
-rw-r--r-- 	 1071 	 Nov 14 05:57 	 LICENSE
-rw-r--r-- 	 8911 	 Nov 14 05:57 	 .gitignore
```
- -t : Display the results sorted by time_modified field (oldest first).
```
$  pyls ./input.json -lt
Total 8
-rw-r--r-- 	 1071 	 Nov 14 05:57 	 LICENSE
-rw-r--r-- 	 83 	 Nov 14 05:57 	 README.md
-rw-r--r-- 	 60 	 Nov 14 08:21 	 go.mod
-rw-r--r-- 	 74 	 Nov 14 08:27 	 main.go
drwxr-xr-x 	 4096 	 Nov 14 09:27 	 token
drwxr-xr-x 	 4096 	 Nov 14 09:51 	 lexer
drwxr-xr-x 	 4096 	 Nov 14 10:28 	 ast
drwxr-xr-x 	 4096 	 Nov 17 07:21 	 parser
```
- -h : Display the file sizes in human readable format.
```
$  pyls ./input.json -Altrh
Total 9
drwxr-xr-x 	 4K 	 Nov 17 07:21 	 parser
drwxr-xr-x 	 4K 	 Nov 14 10:28 	 ast
drwxr-xr-x 	 4K 	 Nov 14 09:51 	 lexer
drwxr-xr-x 	 4K 	 Nov 14 09:27 	 token
-rw-r--r-- 	 74B 	 Nov 14 08:27 	 main.go
-rw-r--r-- 	 60B 	 Nov 14 08:21 	 go.mod
-rw-r--r-- 	 83B 	 Nov 14 05:57 	 README.md
-rw-r--r-- 	 1K 	 Nov 14 05:57 	 LICENSE
-rw-r--r-- 	 8.7K 	 Nov 14 05:57 	 .gitignore
```
- --filter : Filter the output based on given options: file or dir.
```
$  pyls ./input.json -Al --filter dir
Total 4
drwxr-xr-x 	 4096 	 Nov 14 10:28 	 ast
drwxr-xr-x 	 4096 	 Nov 14 09:51 	 lexer
drwxr-xr-x 	 4096 	 Nov 17 07:21 	 parser
drwxr-xr-x 	 4096 	 Nov 14 09:27 	 token
```
- --help : Show help message and exit.

