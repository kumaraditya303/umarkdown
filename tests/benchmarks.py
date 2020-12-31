# -*- coding: utf-8 -*-
import platform
import sys
import timeit
from importlib.metadata import version  # type:ignore

import matplotlib.pyplot as plt
import numpy as np

TEST_DATA = (
    """
# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


## Horizontal Rules

___

---

***


## Typographic replacements

Enable typographer option to see result.

(c) (C) (r) (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,,  -- ---

"Smartypants, double quotes" and 'single quotes'


## Emphasis

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~


## Blockquotes


> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.


## Lists

Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar


## Code

Inline `code`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


Block code "fences"

```
Sample text here...
```

Syntax highlighting

``` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```


## Links

[link text](http://example.com)

[link with title](http://example.com/ "title text!")

Autoconverted link http://example.com/


## Images

![Minion](https://octodex.github.com/images/minion.png)
![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

![Alt text][id]

With a reference later in the document defining the URL location:

[id]: https://octodex.github.com/images/dojocat.jpg  "The Dojocat"

"""
    * 500
)


def main():
    print("Ultra Markdown parsing time compared to other popular Markdown parsers.")
    print()
    print("~~~~~~~~~~~~~")
    print("Test Machine:")
    print("~~~~~~~~~~~~~")
    print()
    uname_system, _, uname_release, uname_version, _, uname_processor = platform.uname()
    print(uname_system, uname_release, uname_processor, uname_version)
    print()
    print("~~~~~~~~")
    print("Version:")
    print("~~~~~~~~")
    print()
    print(
        "- {} {}".format(
            platform.python_implementation(), sys.version.replace("\n", "")
        )
    )
    print(f'- python-markdown    : {version("markdown")}')
    print(f'- python-markdown2   : {version("markdown2")}')
    print(f'- umarkdown          : {version("umarkdown")}')

    umarkdown_code = f"""
from umarkdown import markdown
markdown({TEST_DATA!r})
    """

    markdown_code = f"""
from markdown import markdown
markdown({TEST_DATA!r})
    """
    markdown2_code = f"""
from markdown2 import markdown
markdown({TEST_DATA!r})
    """
    umarkdown_time = timeit.timeit(stmt=umarkdown_code, number=10)
    python_markdown_time = timeit.timeit(stmt=markdown_code, number=10)
    python_markdown_2_time = timeit.timeit(stmt=markdown2_code, number=10)
    x = np.array(["Ultra Markdown", "Python-Markdown", "Python-Markdown2"])
    y = np.array(
        [1 / umarkdown_time, 1 / python_markdown_time, 1 / python_markdown_2_time]
    )
    plt.figure(figsize=(9, 7))
    plt.bar(x, y)
    plt.title(
        "Test Machine: \n"
        f"{uname_system} {uname_release} { uname_processor} { uname_version}\n\n"
        "Version: \n"
        "- {} {}\n".format(
            platform.python_implementation(), sys.version.replace("\n", "")
        )
        + f'- python-markdown: {version("markdown")}\n'
        f'- python-markdown2: {version("markdown2")}\n'
        f'- umarkdown: {version("umarkdown")}\n\n'
        "Test File Size: 1MB\n\n",
        fontweight="bold",
    )
    plt.ylabel("MB/s")
    plt.xlabel("Markdown parsers")
    plt.savefig(
        "docs/images/benchmarks.svg", bbox_inches="tight", dpi=1000, pad_inches=1
    )
    print("Benchmarks report saved to docs/images/benchmarks.svg")


if __name__ == "__main__":
    main()
