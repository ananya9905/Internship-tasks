# Day 6 – Python Utility Packages

## Overview
This project contains a collection of small Python utilities designed to simplify common programming tasks.

## Utilities Included

### 1. Retry Decorator
**File:** `retry_decorator.py`

A decorator that retries a function when an exception occurs, up to a specified number of attempts.

### 2. Timing Decorator
**File:** `timing_decorator.py`

A decorator that measures the execution time of a function.

### 3. File Context Manager
**File:** `context_manager.py`

A context manager for handling file operations and ensuring the file is closed when the context exits.

### 4. File Generator
**File:** `generator.py`

A generator that reads a file line by line, helping process large files without loading the entire file into memory.

## Concepts Practiced
- Python decorators
- Exception handling
- Context managers
- Generators
- File handling
- Type hints

## Folder Structure

```text
Utility Packages/
├── context_manager.py
├── generator.py
├── retry_decorator.py
└── timing_decorator.py
```

## Goal
To practice building reusable Python utilities and writing modular code.