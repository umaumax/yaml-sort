# yaml-sort

## how to use
```
./yaml-sort.py in.yml
./yaml-sort.py in.yml out.yml
```

### yaml-diff
```
diff -U 100 <(./yaml-sort.py sample1.yml) <(./yaml-sort.py sample2.yml)
```

## TODO
* pip download
  * FYI: [umaumax/gtrans]( https://github.com/umaumax/gtrans )

----

[test.yml]
```
#%YAML:1.0
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

```
abc: {x:[12,3]}
```
