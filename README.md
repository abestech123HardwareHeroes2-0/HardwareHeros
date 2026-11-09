# Hardware Heroes 2.0

A Python utility that detects and displays basic hardware information for the machine it runs on, including CPU, RAM, and operating system details.

## Features

- CPU information
- Physical CPU core and logical thread counts
- Total installed RAM
- Operating system and version

## Requirements

- Python 3.9 or later
- [psutil](https://pypi.org/project/psutil/)

## Run locally

From the repository directory, install the dependency and run the script:

```bash
python -m pip install psutil
python detect-hardware.py
```

The results will be printed in your terminal.

## GitHub Actions

The workflow runs the hardware detection script when changes are pushed to the `main` branch. You can also start it manually from the repository’s **Actions** tab.

> **Note:** In GitHub Actions, the script reports the GitHub-hosted runner’s hardware—not your personal computer’s hardware.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for the full terms. The software is provided without warranty, as described in the license.
