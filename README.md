# yaml-sort

sort yaml file (even generated by opencv with bugs)

## how to install
```
# for avoiding 'pip Installing collected packages: UNKNOWN'
pip3 install setuptools --upgrade
pip3 install https://github.com/umaumax/yaml-sort/archive/master.tar.gz
```

## how to use
```
yaml-sort in.yml
yaml-sort in.yml out.yml
```

### yaml-diff
```
diff -U 100 <(yaml-sort sample1.yml) <(yaml-sort sample2.yml)
```

## TODO
* write test code

----

[test.yml]
```
%YAML:1.0
---
set:
   - { x:1, y:2, x:[ 1, 0, 0, 1, 1, 0, 1, 1 ] }
tag:     !!hello
   cols: 3
   rows: 4
   data: [1,-2,3]
abc:     1234
date:    "Fri Jul 26 23:42:37 2019"
```

* `%YAML:x.x`: version
* `---`: データ区切り
  * [YAML Ain’t Markup Language \(YAML™\) Version 1\.2]( https://yaml.org/spec/1.2/spec.html#id2760395 )
* `!!xxx`: tag
  * [YAML Ain’t Markup Language \(YAML™\) Version 1\.2]( https://yaml.org/spec/1.2/spec.html#id2761292 )
    * see: `Secondary Handle`

[The Official YAML Web Site]( https://yaml.org/ )

----

* `%YAML:1.0`: これは正しくは`%YAML 1.0`
  * [YAML Ain’t Markup Language \(YAML™\) Version 1\.2]( https://yaml.org/spec/1.2/spec.html#id2760395 )
    * `%YAML`で検索すると正しい例がヒットする(ただし，このフォーマットが正式かどうかについての定義は見つからず)

* [How to skip lines when reading a yaml file in python? \- Stack Overflow]( https://stackoverflow.com/questions/28058902/how-to-skip-lines-when-reading-a-yaml-file-in-python )
  * 非常に参考になる
* [pyyaml \- yaml\.scanner\.ScannerError: while scanning a directive \- Stack Overflow]( https://stackoverflow.com/questions/15571137/yaml-scanner-scannererror-while-scanning-a-directive )
* [How do I load an OpenCV generated yaml file in python? \- OpenCV Q&A Forum]( https://answers.opencv.org/question/31207/how-do-i-load-an-opencv-generated-yaml-file-in-python/ )

----

## PyYAML
```
pip install -U PyYAML
```

```
yaml.constructor.ConstructorError: could not determine a constructor for the tag 'tag:yaml.org,2002:opencv-matrix'
```
[CloudFormationのYAMLをPyYAMLで読み込む \- GALACTIC1969 \- Medium]( https://medium.com/galactic1969/cloudformation%E3%81%AEyaml%E3%82%92pyyaml%E3%81%A7%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%82%80-eafd5f41bf3c )

## go-yaml/yaml
下記がパースできない

```
%YAML:1.0
```
これは，opencv側のbugらしいので，その点では問題ない

```
abc: {x:[12,3]}
```

----

## FMI
* for pip packaging [umaumax/gtrans]( https://github.com/umaumax/gtrans )
