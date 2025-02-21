# TP1 - on/off adder

## Author: Filipe Santos, A100607

This Python script reads a string and sums all digit sequences found. This behavior can be toggled on and off using specific keywords:

- When the word **off** (case-insensitive) appears, the summing is stopped.

- When the word **on** (case-insensitive) appears, the summing resumes.

- When the **=** symbol appears, the current sum is displayed.

## Usage

The script can be run in two ways:

1. **Reading from standard input (stdin):** If no arguments are passed, the script will read from stdin. `exit` can be typed to terminate the program.

    ```sh
    python adder.py
    ```

2. **Passing a string as an argument:** The script can also process a provided string directly.

    ```sh
    python adder.py "example"
    ```

**Example Input:**
```sh
"10 10 10 = off 50 30 = on example5 ="
```

**Output:**
```sh
(=) 30
(=) 30
(=) 35
```