# Command Line Interface

### **Ultra Markdown** ships out of the box with a simple yet powerful command line interface.

### Install Ultra Markdown with Cli:

```bash
$ pip install umarkdown[cli]
```

### Get more info by asking for help:

```text
$ umarkdown --help

Usage: umarkdown [OPTIONS] FILE DEST

                  ===========================================
                  || Ultra Markdown Command Line Interface ||
                  ===========================================
             Ultra Markdown is an ultrafast Markdown parser written in
                pure C with bindings for Python3.7+. It internally
          uses CMark, an ultrafast C library for parsing Markdown to HTML.

Options:
  --sourcepos      Include source position attribute.
  --hardbreaks     Treat newlines as hard line breaks.
  --nobreaks       Render soft line breaks as spaces.
  --unsafe         Render raw HTML and dangerous URLs.
  --smart          Use smart punctuation.
  --validate-utf8  Replace invalid UTF-8 sequences with U+FFFD.
  --help           Show this message and exit.
```
