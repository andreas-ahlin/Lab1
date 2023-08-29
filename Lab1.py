import csv
import os


class Drama:

    def __init__(self, drama):
        self.dramaName = drama[0]
        self.rating = drama[1]
        self.actors = drama[2]
        self.viewshipRate = drama[3]
        self.genre = drama[4]
        self.director = drama[5]
        self.writer = drama[6]
        self.year = drama[7]
        self.noOfEpisodes = drama[8]
        self.network = drama[9]


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
    print('hej')


main()
