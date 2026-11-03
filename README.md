# Python Log Analyzer
A simple Python project that analyzes server log files and looks for suspicious login activity. It counts failed login attempts for each IP address and flags IPs that have 3 or more failed attempts.

## What It Does

- Reads a log file provided through the command line.
- Counts failed login attempts for each IP address.
- Flags IP addresses with 3 or more failed attempts.
- Displays the results in a simple report.
- Shows an error if the specified file cannot be found.

## How to Use

Make sure you have Python 3 installed.

Open a terminal in the project folder and run:

```bash
python analyzer.py sample.log
```

You can also use a different log file:

```bash
python analyzer.py auth.log
```

If your log file is in another folder, you can provide its path:

```bash
python analyzer.py logs/server.log
```

## Example Output

```text
Failed Logins Report
--------------------
192.168.1.50: 4 failed attempts <--- SUSPICIOUS!

172.16.4.9: 2 failed attempts
```

## Changing the Threshold

The default threshold is 3 failed login attempts. You can change this by editing the `THRESHOLD` variable at the top of `analyzer.py`.

```python
THRESHOLD = 3
```

## Built With

- Python 3
- Dictionaries
- File handling
- argparse

## About

I created this project to practice Python and learn more about analyzing server logs. 
