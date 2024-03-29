# Parsing Options

### **Ultra Markdown** provides you with the following parsing features:

---

- ## **source_pos**

Used to include source position attributes.

```python
>>> from umarkdown import markdown
>>> print(markdown("# Hello World", source_pos=True))
<h1 data-sourcepos="1:1-1:13">Hello World</h1>
```

---

- ## **hard_breaks**

Used to treat newlines as hard line breaks.

```python
>>> from umarkdown import markdown
>>> print(markdown("Hello,\nWorld!", hard_breaks=True))
<p>Hello,<br />
World!</p>
```

---

- ## **no_breaks**

Used to render soft line breaks as spaces.

```python
>>> from umarkdown import markdown
>>> print(markdown("Hello,\n*World*!", no_breaks=True))
<p>Hello, <em>World</em>!</p>
```

---

- ## **unsafe**

Used to render raw HTML and dangerous URLs.

```python
>>> from umarkdown import markdown
>>> print(markdown("<p>Hello World</p>", unsafe=True))
<p>Hello World</p>
```

---

- ## **smart**

Used to use smart punctuation.

```python
>>> from umarkdown import markdown
>>> print(markdown("Hello---", smart=True))
<p>Hello—</p>
```

---
