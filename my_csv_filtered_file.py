import csv


file_name = "imdb-movie-data.csv"
result = []
def muvie_filter(genre):
    with open(file_name) as csvfile:
        csv_content = csv.DictReader(csvfile)
        for muvie in csv_content:
            genres = muvie["Genre"].split(',')
            if genre in genres:
                result.append(muvie)
        return result

print(len(muvie_filter('Western')))