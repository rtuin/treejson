# treejson

This package helps you discover the structure of a JSON string.

## Usage

```bash
$ echo "{\"foo\": {\"bar\": 1, \"baz\": 2 } }" | treejson
.
└── foo
    ├── baz
    └── bar
```

Use `$ treejson --help` to see all possible arguments.

## Install

This package requires Python 2.x.
Use the pip installer to install tree-json.

``` bash
$ (sudo) pip install treejson
```