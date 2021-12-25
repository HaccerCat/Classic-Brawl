import sys
import datetime
from DataBase.SQLManager import DataBase as dB
from Logic.Player import Player
import json
from Utils.Helpers import Helpers
class DB:
    def __init__(self):
        self.player = Player
        self.client = dB("players.sqlite")
        self.clubs = dB("clubs.sqlite")

        self.data = {
            'Name': 'Guest',
            'NameSet': False,
            'Gems': Player.gems,
            'Trophies': Player.trophies,
            'Tickets': Player.tickets,
            'Resources': Player.resources,
            'TokenDoubler': 0,
            'HighestTrophies': 0,
            'HomeBrawler': 0,
            'TrophyRoadReward': 300,
            'ExperiencePoints': Player.exp_points,
            'ProfileIcon': 0,
            'NameColor': 0,
            'UnlockedBrawlers': Player.brawlers_unlocked,
            'BrawlersTrophies': Player.brawlers_trophies,
            'BrawlersHighestTrophies': Player.brawlers_high_trophies,
            'BrawlersLevel': Player.brawlers_level,
            'BrawlersPowerPoints': Player.brawlers_powerpoints,
            'UnlockedSkins': Player.unlocked_skins,
            'SelectedSkins': Player.selected_skins,
            'SelectedBrawler': 0,
            'Region': Player.region,
            'SupportedContentCreator': "Modern Brawl",
            'StarPower': Player.starpower,
            'Gadget': Player.gadget,
            'BrawlPassActivated': False,
            'WelcomeMessageViewed': False,
            'ClubID': 0,
            'ClubRole': 1,
            'TimeStamp': str(datetime.datetime.now())
        }

        self.club_data = {
            'Name': '',
            'Description': '',
            'Region': '',
            'BadgeID': 0,
            'Type': 0,
            'Trophies': 0,
            'RequiredTrophies': 0,
            'FamilyFriendly': 0,
            'Members': [],
            'Messages': []
        }

    def merge(self, dict1, dict2):
        return (dict1.update(dict2))


    def create_player_account(self, id, token):
        auth = {
            'ID': id,
            'Token': token,
        }

        auth.update(self.data)

        self.client.insert(token, auth)


    def load_player_account(self, id, token):
    	result = self.client.load_data(token)
    	if result:
            for x in self.data:
                if x not in result:
                    result[x] = self.data[x]

            return result
    def load_player_account_by_id(self, id):
    	collections = self.client.load_all()
    	for collection in collections:
    		if collection["ID"] == id:
    			return collection

    def update_player_account(self, token, item, value):
        self.client.update(token, item, value)


    def update_all_players(self, query, item, value):
    	collections = self.client.load_all()
    	for collection in collections:
    		self.client.update(collection["Token"], item, value)
    		
    def load_all_players(self, args):
        result = self.client.load_all()
        return result


    def load_all_players_sorted(self, args, element):
        result = self.client.load_all()
        sorter = sorted(result, key=lambda x:x[element], reverse=True)
        return sorter


    def create_club(self, id, data):
        auth = {
            'ID': id,
        }

        auth.update(data)

        self.clubs.insert(id, auth)


    def update_club(self, id, item, value):
        query = {"ID": id}
        self.clubs.update(id, item, value)


    def load_club(self, id):
        query = {"ID": id}
        result = self.clubs.load_data(id)
        return result


    def load_all_clubs_sorted(self, args, element):
    	result = self.clubs.load_all()
    	sorter = sorted(result, key=lambda x:x[element], reverse=True)
    	return sorter

    def load_all_clubs(self, args):
        result = self.clubs.load_all()
        return result

    def delete_club(self, id):
        query = {"ID": id}
        self.clubs.delete(id)
    def close(self):
    	self.client.close()
    	self.clubs.close()
