# Day 4 - Library Management System

## Overview

This project is a simple **Library Management System** developed in Python using Object-Oriented Programming (OOP) concepts.

The program manages:

- Books
- Library members
- Borrowing books
- Returning books
- Book availability

The project also demonstrates the use of Python `dataclasses`, custom methods, `__repr__()`, dictionaries, lists, and object relationships.

---

## Concepts Used

The following Python concepts are implemented in this project:

- Classes and Objects
- Constructors
- Instance attributes
- Instance methods
- `dataclass`
- `field()` with `default_factory`
- Type annotations
- Lists
- Dictionaries
- Conditional statements
- `input()` for user interaction
- Object relationships
- Dunder method `__repr__()`

---

## Classes

### 1. Book

The `Book` class represents a book available in the library.

It is implemented using the `@dataclass` decorator.

### Attributes

| Attribute | Type | Description |
|---|---|---|
| `book_id` | `int` | Unique ID of the book |
| `title` | `str` | Title of the book |
| `author` | `str` | Author of the book |
| `available` | `bool` | Indicates whether the book is available |

The `available` attribute is set to `True` by default.

### Methods

#### `is_borrowed()`

Checks whether the book is currently borrowed.

- Returns `False` if the book is available.
- Returns `True` if the book is not available.

#### `__repr__()`

Provides a readable representation of a `Book` object.

Example:

```text
Book(Book ID: 101, Title: Python Basics, Author: ABC, Available: True)
```