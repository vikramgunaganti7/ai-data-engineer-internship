import argparse
import csv


def main():
	parser = argparse.ArgumentParser(description="Count data rows and empty cells in a CSV file.")
	parser.add_argument("csv_file", help="Path to the CSV file")
	args = parser.parse_args()

	with open(args.csv_file, newline="", encoding="utf-8-sig") as csv_file:
		rows = csv.reader(csv_file)
		next(rows, None)  # Skip the header row.
		row_count = 0
		null_count = 0
		for row in rows:
			row_count += 1
			null_count += sum(value.strip() == "" for value in row)

	print(f"Row count: {row_count}")
	print(f"Null count: {null_count}")


if __name__ == "__main__":
	main()
