# Saturday Interpreter

*Version*: `0.0.1`

Saturday is a stack-based interpreter that allows for various operations, including mathematical calculations, logic operations, and control structures like loops and conditions. This project is currently in development, and this README serves as a temporary guide for users and contributors.

## Features

- Stack-based computation
- Arithmetic and logical operations 
- Loop and conditional control structures
- Debug mode for step-by-step execution

## Installation

To get started with `Saturday`, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-repo/saturday.git
cd saturday
```

2. Install the required dependencies (if any):

```bash
pip install -r requirements.txt
```

3. Run the interpreter:

```bash
python saturday.py <path_to_source_file>
```
You can also enable debug mode by adding the `--debug` flag:

```bash
python saturday.py --debug <path_to_source_file>
```

## Usage

### Basic Example

Here's a quick example to showcase the capabilities of `Saturday`. Consider the following code snippet:

```plaintext
1 2 +
```

This will push `1` and `2` onto the stack, and then the `+` operator will pop these values and push the result `3`.

### Hello World in saturday

Here is an example code that outputs the string "hello world":

```plaintext
849+*d`o # 'h'
3s-d`o   # 'e'
7+d`o    # 'l'
d`o      # 'l'
d3+d`o   # 'o'
48*`o    # ' '
d8+`o    # 'w'
`o       # 'o'
d6+`o    # 'r'
d`o      # 'l'
8s-`o    # 'd'
25*`o    # '\n'
```

### Commands

| Command | Pops  | Description                                                               |
|---------|-------|---------------------------------------------------------------------------|
| !       | x     | Push not x                                                                |
| %       | x, y  | Push x modulo y                                                           |
| &       | x, y  | Push x & y                                                                |
| (       | None  | Beginning of a loop                                                       |
| )       | None  | End of a loop                                                             |
| *       | x, y  | Push x * y                                                                |
| +       | x, y  | Push x + y                                                                |
| -       | x, y  | Push x - y                                                                |
| /       | x, y  | Push x / y                                                                |
| 0-9     | None  | Push the respective number onto the stack                                 |
| <       | x, y  | Push x < y                                                                |
| =       | x, y  | Push x = y                                                                |
| >       | x, y  | Push x > y                                                                |
| C       | x     | Push ceil(x)                                                              |
| D       | x     | Push x's denominator                                                      |
| F       | x     | Push x! (factorial)                                                       |
| I       | x     | Push int(x) (floor(x))                                                    |
| N       | x     | Push x's numerator                                                        |
| O       | x     | Push the ordinal of x                                                     |
| R       | x     | Push round(x) (Round to nearest integer)                                  |
| S       | x     | Push str(x)                                                               |
| T       | x     | Push trunc(x)                                                             |
| [       | x     | Beginning of an if-statement (if x)                                       |
| ]       | None  | End of an if-statement                                                    |
| ^       | x, y  | Push x ^ y                                                                |
| `       | x     | Push a character with ordinal x                                           |
| b       | None  | Break (terminate the nearest enclosing loop)                              |
| c       | None  | Continue (continue with the next cycle of the nearest enclosing loop)      |
| d       | x     | Push x twice                                                              |
| g       | x     | Swap the stack top with the x-th element in the stack (after popping)      |
| i       | None  | Push the ordinal of the next character in the input (-1 if exhausted)      |
| o       | x     | Output x                                                                  |
| p       | x     | Do nothing                                                                |
| s       | x, y  | Push x, then push y                                                       |
| t       | None  | Terminate the program immediately                                         |
| x       | x     | Push the x-th element in the stack (after popping)                        |
| |       | x, y  | Push x | y                                                                |
| ~       | x     | Push ~x                                                                   |


### Control Structures

- *Loops*: Loops are enclosed in `(` and `)` brackets. You can use loop control commands like `b` (break) and `c` (continue).
- *Conditions*: Conditional checks are done with `[` and `]` brackets, and logical comparisons like `<`, `>`, `=`.

## Contributing

This README file is temporary and will likely be replaced with a more detailed document in the near future. In the meantime, feel free to explore the code, experiment with the interpreter, and contribute to the project!

You can view our [wiki](https://github.com/cyan-ice/saturday/wiki) for more detailed information and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/cyan-ice/saturday/blob/main/LICENSE) file for more information.
