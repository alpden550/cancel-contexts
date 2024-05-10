# Cancel-contexts

[![CI/RUFF/TESTS](https://github.com/alpden550/cancel-contexts/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/alpden550/cancel-contexts/actions/workflows/python-app.yml)
[![PyPI version](https://badge.fury.io/py/cancel-contexts.svg)](https://badge.fury.io/py/cancel-contexts)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/cancel-contexts)](https://pypi.org/project/cancel-contexts/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cancel-contexts)](https://pypi.org/project/cancel-contexts/)
[![PyPI - License](https://img.shields.io/pypi/l/cancel-contexts)](https://github.com/alpden550/cancel-contexts/blob/main/LICENSE)
[![PyPI - Status](https://img.shields.io/pypi/status/cancel-contexts)](https://pypi.org/project/cancel-contexts/)
 
This is a simple implementation of cancel-contexts (cancel tokens is C#) in Python. It is inspired by the Go programming language's context package.

- CancelContext is a simple class that can be used to manually cancel.
- TimeoutContext is a simple class that can be used to cancel a context after a certain amount of time.

`cancel()` - manually cancel the context.

`cancelled` - a property that returns True if the context is canceled.

`bool()` - returns True if the context is not canceled or condition is relevant.

`check_cancelled()` - raises actual BaseCancelContextError if the context is canceled or condition isn't relevant.


## Installation

```bash 
poetry add cancel-contexts
```

or

```bash
pip install cancel-contexts
```


## Usage

```python
from cancel_contexts import CancelContext

ctx = CancelContext()
print(ctx.cancelled) # False
print(bool(ctx)) # True

ctx.cancel()
print(ctx.cancelled) # True
print(bool(ctx)) # False
```

```python
from cancel_contexts import CancelContext
from cancel_contexts.exceptions import ContextCancelledError

ctx = CancelContext()
counter = 0
while ctx:
    counter += 1
    if counter == 10:
        ctx.cancel()

print(ctx.cancelled) # True

try:
    ctx.check_cancelled()
except ContextCancelledError as e:
    print(e) # Context was cancelled
```


```python
from time import sleep
from cancel_contexts import TimeOutContext
from cancel_contexts.exceptions import ContextTimeOutError

ctx = TimeOutContext(10)

print(ctx.cancelled) # False

while ctx:
    sleep(1)
    print(ctx.cancelled) # False

print(ctx.cancelled) # True
try:
    ctx.check_cancelled()
except ContextTimeOutError as e:
    print(e) # Context was timed out
```
