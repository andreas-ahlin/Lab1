import csv


class Drama:

    def __init__(self, drama):
        self.dramaName = drama[0]
        self.rating = float(drama[1])
        self.actors = drama[2]
        self.viewshipRate = float(drama[3])
        self.genre = drama[4]
        self.director = drama[5]
        self.writer = drama[6]
        self.year = int(drama[7])
        self.noOfEpisodes = int(drama[8])
        self.network = drama[9]

    def __str__(self):
        return 'Namn: ' + self.dramaName + '\n' + 'Rating: ' + str(self.rating) + '\n' + 'Actors: ' + self.actors + '\n' + 'viewshipRate :' + str(self.viewshipRate) + '\n' + 'Genre :' + self.genre + '\n' + 'Director: ' + self.director + '\n' + 'Writer : ' + self.writer + '\n' + 'Year :' + str(self.year) + '\n' + 'NoOfEpisodes :' + str(self.noOfEpisodes) + '\n' + 'Network : ' + self.network

    def __lt__(self, other):
        return self.rating < other.rating

    def check_rating_8(self):
        if self.rating > 8:
            return True
        else:
            return False

    def check_year_2020(self):
        if self.year > 2020:
            return True
        else:
            return False


def read_file():
    listofdrama = []
    with open('kdrama.csv', newline='') as dramafile:
        csvfile = csv.reader(dramafile, delimiter=',')
        next(csvfile)
        for line in csvfile:
            newdrama = Drama(line)
            listofdrama.append(newdrama)
    return listofdrama


def read_file_to_list():
    with open('kdrama.csv', newline='') as dramafile:
        csvfile = csv.reader(dramafile, delimiter=',')
        next(csvfile)
        listofdrama = list(csvfile)
    return listofdrama


def search_new_drama(listofdramaobject):
    list2020 = []
    for item in listofdramaobject:
        if item.check_year_2020():
            list2020.append(item)
    return list2020


def main():
    dramalist1 = read_file_to_list()
    drama1 = Drama(dramalist1[0])
    drama2 = Drama(dramalist1[1])
    print(drama1)
    print(drama2)
    print(drama1 < drama2)
    print(drama1.check_rating_8())
    print(drama1.check_year_2020())

    dramaobjectlist = read_file()
    list2020 = search_new_drama(dramaobjectlist)
    for item in list2020:
        print(item.dramaName)


main()
