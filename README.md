## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the script

Ensure all csv files you want processed are in the `files_to_process` directory. Then run
```bash
python main.py
```
and the processed csvs will be in the directory `processed_csvs`.
