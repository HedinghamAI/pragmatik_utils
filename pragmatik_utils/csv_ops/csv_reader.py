import csv

def read_all_rows(file, contains_headers=True, delimiter=",", quotechar='"'):
    data = []
    with open(file, "r") as fin:
        reader = csv.reader(fin, delimiter=delimiter, quotechar=quotechar)
        headers = []
        if contains_headers:
            headers = next(reader, None)

        for row in reader:
            if not contains_headers and headers == []:
                headers = ["{}".format(i) for i in range(0, len(row))]
            row_dict = dict(zip(headers, row))
            data.append(row_dict)
    return data
