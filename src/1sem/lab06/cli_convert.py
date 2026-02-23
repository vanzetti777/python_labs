import argparse
import os
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="json в csv")
    # подаргументы in и out для args входных и выходных
    p1.add_argument("--in", dest="input", required=True, help="путь для json")
    p1.add_argument("--out", dest="output", required=True, help="путь для csv")

    p2 = sub.add_parser("csv2json", help="путь csv в json")
    p2.add_argument("--in", dest="input", required=True, help="путь для csv")
    p2.add_argument("--out", dest="output", required=True, help="путь для json")

    p3 = sub.add_parser("csv2xlsx", help="путь csv в xlsx")
    p3.add_argument("--in", dest="input", required=True, help="путь для csv")
    p3.add_argument("--out", dest="output", required=True, help="путь для xlsx")

    args = parser.parse_args()
    # Проверка входного файла
    if not os.path.exists(args.input):
        parser.error("входной файл не найден.")

    # Выполнение подкоманды
    try:
        # если команда такая то такая то, то из 5 лабы
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")
    except Exception as e:
        parser.error("ошибка при конвертации")


if __name__ == "__main__":
    main()
