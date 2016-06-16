#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright (c) 2016 Richard Tuin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import json
import getopt
import sys

def treejson():
    opts, args = getopt.getopt(sys.argv[1:], "L:h", ["help"])

    depth = 999
    for opt, arg in opts:
        if opt == "-L":
            depth = int(arg)
        if opt in ("--help", "-h"):
            print "Usage: treejson [-L level] < example.json"
            print "\nPossible arguments:"
            print "  -L level\tDescend only level nodes deep."
            sys.exit()

    try:
        structure = json.load(sys.stdin)
    except ValueError:
        print "Please feed me a valid JSON document."
        sys.exit(1)


    def show_structure(root, level=1, indent_chars=""):
        index = 0

        use_index_as_key = isinstance(root, list)

        for key in root:
            if use_index_as_key:
                value = key
                key = str(index)
            else:
                value = root[key]

            has_children = hasattr(value, '__len__') and not isinstance(value, basestring)

            if index+1 == len(root):
                tree_char = u"└"
            else:
                tree_char = u"├"

            print indent_chars + tree_char + u"── " + key + (" []" if isinstance(value, list) else "")

            if has_children and level < depth:
                if len(root) > 1 and index+1 < len(root):
                    new_indent_chars = indent_chars + u"│" + "   "
                else:
                    new_indent_chars = indent_chars + "    "
                show_structure(value, level=level+1, indent_chars=new_indent_chars)
            index += 1

    print "." + (" []" if isinstance(structure, list) else "")
    show_structure(structure)