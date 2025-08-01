import urllib.request
import os
import csv
import time

'''a = Hopto()
a.map_openall()
a.search("BionicRex_Character_BP_C")
print(a.sort("melee"))
'''

class Hopto:
    stats = ['id', 'creature', 'gender', 'lvl', 'lat', 'lon', 'hp', 'stam', 'melee', 'weight', 'speed', 'food', 'oxy', 'craft', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'ccc', 'dinoid', 'tameable', 'trait', 'map']
    maps = {
        "Abberation":"http://wiredcat.hopto.org/WiredcatAberration/Wild.txt",
        "Center":"http://wiredcat.hopto.org/WiredcatCenter/Wild.txt",
        "Crystal_Isles":"http://wiredcat.hopto.org/WiredcatCrystal/Wild.txt",
        "Extinction":"http://wiredcat.hopto.org/WiredcatExtinction/Wild.txt",
        "Fjordur":"http://wiredcat.hopto.org/WiredcatFjordur/Wild.txt",
        "Genesis":"http://wiredcat.hopto.org/WiredcatGenesis/Wild.txt",
        "The_Island":"http://wiredcat.hopto.org/WiredcatIsland/Wild.txt",
        "Lost_Island":"http://wiredcat.hopto.org/WiredcatLostIsland/Wild.txt",
        "Ragnarok":"http://wiredcat.hopto.org/WiredcatRagnarok/Wild.txt",
        "Scortched_Earth":"http://wiredcat.hopto.org/WiredcatScorchedEarth/Wild.txt",
        "Valguero":"http://wiredcat.hopto.org/WiredcatValguero/Wild.txt"
    }

    def __init__(self, map_choice=None):
        self.map_choice = map_choice
        self.map_data = []
        self.search_results = []

    def fetch(self):
        # download and store maps
        if os.path.isdir("hopto_data"):
            pass
        else:
            os.mkdir("hopto_data")
        for map_ in self.maps:
            print(f'Fetching {map_}...')
            urllib.request.urlretrieve(Hopto.maps[map_], os.path.join('hopto_data', '{}.csv'.format(map_)))
            time.sleep(1) # don't overwealm the servers

    def map_open(self):
        if self.map_choice == None:
            return None
        with open(os.path.join('hopto_data', '{}.csv'.format(self.map_choice))) as map_file:
            map_csv = csv.reader(map_file)
            map_data = list(map_csv)[1:]
            self.map_data = [row + [self.map_choice] for row in map_data]
            return self.map_data
        
    def map_openall(self):
        all_maps = []
        for map_l in self.maps.keys():
            p = Hopto(map_l).map_open()
            all_maps += p
        self.map_data = all_maps
        return self.map_data

    def get_list(self):
        if self.map_data == []:
            return None
        characters = []
        for character in self.map_data:
            if character[1] not in characters:
                characters.append(character[1])
        return characters

    def search(self, name):
        hoptos = []
        for character in self.map_data:
            if character[1] == name:
                hoptos.append(character)
        self.search_results = hoptos
        return self.search_results

    def sort(self, stat, high_to_low=True):
        self.search_results =  sorted(self.search_results, key=lambda x: float(x[self.stats.index(stat)]), reverse=high_to_low)
        return self.search_results