
![](https://www.jaimedcsilva.com/static/img/python.png)
# jaime38130 


A simple Python library to print colored text in the terminal using ANSI escape codes.

> Lightweight, easy to use, and perfect for CLI tools, scripts, and debugging output.

---

## Installation

```bash
pip install jaime38130
```

---

## Import

```python
from jaime38130 import *
```

---

## Examples

### Basic

```python
green("I needed color")
```

![](https://www.jaimedcsilva.com/static/img/jaime38130/standard.png)

---

### Header style

```python
green("I needed color", "header")
```

![](https://www.jaimedcsilva.com/static/img/jaime38130/header.png)

---

### Bottom spacing

```python
green("I needed color", "*")
```

![](https://www.jaimedcsilva.com/static/img/jaime38130/bottom.png)

---

### Top & bottom spacing

```python
green("I needed color", "**")
```

![](https://www.jaimedcsilva.com/static/img/jaime38130/top_bottom.png)

---

## Available colors

```python
green()
white()
black()
cyan()
magenta()
red()
blue()
yellow()
```

---

## Bonus

```python
hidden_secret()
```

---

## About

This package was created to make terminal output more readable and visually structured in Python scripts and console applications.