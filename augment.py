import pandas as pd
import sys

def duplicate_except_medical_concerns():
    # Read CSV from stdin
    df = pd.read_csv(sys.stdin)

    # Add row_id to preserve original positions (1-indexed)
    df = df.reset_index().rename(columns={'index': 'row_id'})
    df['row_id'] += 1

    # Separate Medical Concerns to preserve original rows
    medical_concerns = df[['row_id', 'Medical Concerns']]

    # Drop Medical Concerns for duplication
    to_duplicate = df.drop(columns=['Medical Concerns'])

    # Duplicate each row 3 times
    duplicated_rows = to_duplicate.loc[to_duplicate.index.repeat(3)].copy()

    # Compute new row_ids: (original - 1) * 3 + i
    duplicated_rows['row_id'] = (
        (duplicated_rows['row_id'] - 1) * 3 +
        duplicated_rows.groupby('row_id').cumcount() + 1
    )

    # Merge Medical Concerns back, preserving original row_id
    final_df = pd.merge(
        duplicated_rows,
        medical_concerns,
        on='row_id',
        how='outer'
    ).sort_values('row_id').reset_index(drop=True)

    # Output to stdout
    final_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    duplicate_except_medical_concerns()