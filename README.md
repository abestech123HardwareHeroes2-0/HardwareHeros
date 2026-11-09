# Hardware Heroes 2.0

A simple Python script that reports basic hardware and operating-system information for the computer where it runs.

## What it reports

- CPU information
- CPU core and thread counts
- Installed RAM
- Operating system and version

## Run it on your computer

You need Python installed. From the repository directory, install the dependency and run the script:

```bash
python -m pip install psutil
python detect-hardware.py
```

The script prints the results in your terminal.

## GitHub Actions

This repository includes a GitHub Actions workflow that runs the script when code is pushed to the `main` branch. You can also start it manually from the **Actions** tab.
## License limitations

This software is provided “as is,” without warranty of any kind. The authors are not liable for claims or damages arising from its use. See the [MIT License](LICENSE) for the full terms.

**Note:** When GitHub Actions runs the script, it reports information about GitHub’s runner machine—not your personal computer.

## License

This project is available under the MIT License. See [LICENSE](LICENSE).
