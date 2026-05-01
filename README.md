## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the script

1. Remove all test csv files from the `files_to_process` directory
```bash
rm files_to_process/*
```
1. Ensure all csv files you want processed are in the `files_to_process` directory.
1. Run
```bash
python main.py
```
and the processed csvs will be in the directory `processed_csvs`.
