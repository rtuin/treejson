# treejson

This package helps you discover the structure of a JSON string.

## Usage

```bash
$ echo "{\"foo\": {\"bar\": 1, \"baz\": 2 } }" | treejson
.
└── foo
    ├── baz
    └── bar

$ curl https://api.github.com/users/rtuin/orgs | treejson
. []
├── 0
│   ├── issues_url
│   ├── members_url
│   ├── description
│   ├── ...
└── ...
    ├── ...
    ├── ...
```

Use `$ treejson --help` to see all possible arguments.

## Install

This package requires Python 2.x.
Use the pip installer to install tree-json.

``` bash
$ (sudo) pip install treejson
```

## Changelog

All notable changes are documented in the [changelog file](CHANGELOG.md).

## Credits

- [Richard Tuin](https://github.com/rtuin)
- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see the [license file](LICENSE) for more information.
