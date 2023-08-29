import csv
import os


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


def read_file():
    listofdrama = []
    with open('kdrama.csv', newline='') as dramafile:
        csvfile = csv.reader(dramafile, delimiter=',')
        next(csvfile)
        for line in csvfile:
            newdrama = Drama(line)
            listofdrama.append(newdrama)

    return listofdrama


def main():
    dramalist = read_file()
    print(dramalist[1])
    print(dramalist[1] < dramalist[2])


main()
