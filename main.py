from utils import reading_file, get_filtered_date, get_last_values, get_formatted_date


def main():
    FILTER_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5

    data = reading_file()
    data = get_filtered_date(data, filter_empty_from=FILTER_EMPTY_FROM)
    data = get_last_values(data, count_last_values=COUNT_LAST_VALUES)
    data = get_formatted_date(data)
    print("INFO: Вывод транзакций...")
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
