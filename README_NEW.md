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

### Control Structures

    *Loops*: Loops are enclosed in `(` and `)` brackets. You can use loop control commands like `b` (break) and `c` (continue).
    *Conditions*: Conditional checks are done with `[` and `]` brackets, and logical comparisons like `<`, `>`, `=`.

## Contributing

This README file is temporary and will likely be replaced with a more detailed document in the near future. In the meantime, feel free to explore the code, experiment with the interpreter, and contribute to the project!

You can view our [wiki](https://github.com/cyan-ice/saturday/wiki) for more detailed information and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/cyan-ice/saturday/blob/main/LICENSE) file for more information.
