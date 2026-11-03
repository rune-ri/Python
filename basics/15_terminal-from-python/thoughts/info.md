# Python: Operating System Interaction

Python provides different modules for interacting with the operating system and running external programs.

Two important modules are:

- `os`
- `subprocess`

Both can perform operations that are commonly associated with terminal usage, but they do so through different mechanisms.

## 1. `os` — Direct Operating System Interaction

The `os` module provides Python interfaces to operating-system functionality.

Python uses these interfaces to request information or operations directly from the operating system.

Examples:

```python
import os

os.getcwd()          # Get current working directory
os.listdir(".")      # List directory contents
os.mkdir("test")     # Create a directory
os.getpid()          # Get current process ID
```

The important distinction is that Python calls predefined functions rather than executing terminal commands.

The available operations depend on the functionality exposed by the `os` module.

This does not mean that `os` is inherently less flexible. It means that its functionality is accessed through specific Python functions and their defined parameters.

The underlying operating-system operations are handled by the OS. Python does not need to manage their internal implementation.

## 2. `subprocess` — External Process Execution

The `subprocess` module allows Python to create and manage additional processes.

Python requests the operating system to launch another program, which executes independently of the Python process.

Example:

```python
import subprocess

subprocess.run(["ls", "-l"])
```

Here:
1. Python calls `subprocess.run()`.
2. The operating system creates a new process.
3. The new process executes the `ls` program with `-l` as an argument.
4. The process finishes and returns its execution result.

Unlike `os`, `subprocess` allows Python to execute external programs directly.

This makes it possible to use many programs and utilities that are available on the operating system.

### Managing the process

Python can also interact with the process it launches:

```python
result = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.returncode)
```

Python can capture standard output, standard error and the return code.

### Shell execution

By default, `subprocess.run()` does not execute commands through a shell.

For example:

```python
subprocess.run(["ls", "-l"])
```

To use shell functionality such as pipes (`|`), redirection (`>`) and shell variable expansion, a shell must be explicitly invoked.

```python
subprocess.run("ls -l | grep test", shell=True)
```

## 3. Architectural Difference

The distinction can be understood as:

- `os`: Python directly uses operating-system interfaces to perform operations.
- `subprocess`: Python asks the operating system to launch another process, which performs its own operations.

This can be visualized as:

```text
OS MODULE

Python Process
      |
      | OS interface
      v
Operating System
      |
      v
Resources / Services
```

```text
SUBPROCESS MODULE

Python Process
      |
      | Request process creation
      v
Operating System
      |
      | Launches
      v
External Process
      |
      | OS interface
      v
Operating System
```

## 4. Important Notes

- Neither module requires an open terminal window.
- Both can operate in the background.
- `os` does not execute terminal commands.
- `subprocess` executes external programs, not necessarily terminal commands.
- `subprocess` can capture and manage the output of external processes.
- `os` and `subprocess` can both interact with operating-system functionality, but through different interfaces.

**Core distinction:** `os` provides Python with operating-system functionality, whereas `subprocess` provides Python with the ability to launch and manage other programs.
