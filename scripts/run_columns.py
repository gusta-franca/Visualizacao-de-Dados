import argparse
import json
import pathlib

from src.columns import columns_matrix, columns_summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage = "run_columns.py [--src PATH] [--out PATH] [--start YEAR] [--end YEAR]",
        description = "Compute commmon columns for datasets in a given year range"
    )

    parser.add_argument("--src", type = pathlib.Path, default = pathlib.Path("data/raw"))
    parser.add_argument("--out", type = pathlib.Path, default = pathlib.Path("data/processed"))
    parser.add_argument("--start", type = int, default = 1979)
    parser.add_argument("--end", type = int, default = 2026)

    args = parser.parse_args()

    summary = columns_summary(args.src, args.start, args.end)
    summary_path = args.out / f"column_summary_{args.start}_{args.end}.json"

    with open(summary_path, "w") as file_path:
        json.dump(summary, file_path, indent = 4)

    print(f"Sumário das colunas salvo em {summary_path}")

    matrix = columns_matrix(args.src, args.start, args.end)
    matrix_path = args.out / f"column_matrix_{args.start}_{args.end}.csv"

    matrix.to_csv(matrix_path)

    print(f"Matriz das colunas salvo em {matrix_path}")

