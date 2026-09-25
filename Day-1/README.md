# Day 1 - Unit Converter

## What the program does

This is a menu-driven Python Unit Converter program. It converts values between different units of:

* Temperature
* Distance
* Weight

The program accepts both menu numbers and menu names, and displays an error message for invalid choices or unsupported unit combinations.

### Supported Conversions

**Temperature**

* Celsius ↔ Fahrenheit
* Celsius ↔ Kelvin
* Fahrenheit ↔ Kelvin

**Distance**

* Metres (m)
* Kilometres (km)
* Centimetres (cm)
* Miles

**Weight**

* Grams
* Kilograms (kg)
* Pounds

## How to Run

Open the `Day-1` folder in the terminal and run the Python file:

```bash
python unit_converter.py
```

## Sample Run

```text
===== UNIT CONVERTER =====

1. Temperature
2. Distance
3. Weight
4. Exit

Enter your choice: 1

Enter temperature: 25
Enter the unit of Temperature: celsius
Enter the unit of temperature to convert in: fahrenheit

25.0 celsius is equals to 77.0 fahrenheit.

===== UNIT CONVERTER =====

1. Temperature
2. Distance
3. Weight
4. Exit

Enter your choice: 2

Enter distance: 5
Enter the unit of distance: km
Enter the desired unit to be converted: miles

5.0 km is equals to 3.106855 miles.

===== UNIT CONVERTER =====

1. Temperature
2. Distance
3. Weight
4. Exit

Enter your choice: 3

Enter weight: 1000
Enter unit of weight: grams
Enter unit of weight to convert in: kg

1000.0 grams is equals to 1.0 kg
```

## Concepts Used

* Functions
* `if` / `elif` / `else`
* User input with `input()`
* Type conversion using `float()`
* String methods such as `lower()` and `strip()`
* `while` loop
* Basic arithmetic and unit conversion formulas
* Function return values
