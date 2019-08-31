---
title: 'shell中括号使用总结'
date: 2017-08-14 20:19:45
tags: [cs]
published: true
hideInList: false
feature: 
---

# ${var}

限定变量名称范围

``` bash
#!/bin/sh
# test.sh
var=test
echo ${var}12
```

效果如下

``` bash
$ ./test.sh
$ var12
```

# $(cmd)

命令替换

``` bash
#!/bin/sh
# test.sh
echo $(ls)
```

运行效果与 `ls` 相同

# {}或()

一串命令的执行

``` bash
$ { echo 1;echo "A";} > tmp
$ cat ./tmp
$ 1
$ A
```

# \${var:-string},\${var:+string},\${var:=string},\${var:?string}

几种特殊的替换结构

## ${var:-string}
若`var`为空，则结果为`"string"`，否则结果为`$var`。

## ${var:=string}
若`var`为空，则结果为`"string"`，并将该字符串赋给`var`，否则结果为`$var`。

## ${var:+string}
若`var`不为空，则结果为`"string"`，否则结果为`$var`。

## ${var:?string}
若`var`不为空，则结果为`$var`，否则将`"string"`输出到标准错误中，并从脚本退出。

# $((exp))

POSIX标准的扩展计算，只要符合C的运算符都可用在$((exp))，甚至是三目运算符。

# \${var%pattern},\${var%%pattern},\${var#pattern},\${var##pattern}

四种模式匹配替换结构

# []或[[]]

类似test

# ()

在子shell中运行

# {}

{1..30} 就是1-30，或者是/{,s}bin/表示/bin/和/sbin/，ab{c,d,e}表示abc、abd、abe

>[reference](http://www.jb51.net/article/60326.htm)
