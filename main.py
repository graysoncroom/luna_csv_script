from pathlib import Path
import pandas as pd

csv_files = list(Path('./files_to_process').glob('*.csv'))

for csv_file in csv_files:
    df = pd.read_csv(csv_file, encoding='utf-8-sig')
    df['email'] = df['username'].fillna('').apply(
        lambda username: username + '@syr.edu' if username.strip() else ''
    )
    df.to_csv(f'./processed_files/{csv_file.stem}_with_emails.csv', index=False)
