from ByteStream.Writer import Writer

class BattleResultMessage(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.db = db

    def encode(self):
        self.writeVInt(2)

        self.writeVInt(self.player.rank) # player rank

        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        old_tr = self.player.trophies


        if 0 <= brawler_trophies <= 49:
            rank_1_val = 10
            rank_2_val = 8
            rank_3_val = 7
            rank_4_val = 6
            rank_5_val = 4
            rank_6_val = 2
            rank_7_val = 2
            rank_8_val = 1
            rank_9_val = 0
            rank_10_val = 0
        else:
            if 50 <= brawler_trophies <= 99:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 2
                rank_7_val = 2
                rank_8_val = 0
                rank_9_val = -1
                rank_10_val = -2

            if 100 <= brawler_trophies <= 199:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -1
                rank_9_val = -2
                rank_10_val = -2

            if 200 <= brawler_trophies <= 299:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -2
                rank_9_val = -3
                rank_10_val = -3

            if 300 <= brawler_trophies <= 399:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = 0
                rank_7_val = 0
                rank_8_val = -3
                rank_9_val = -4
                rank_10_val = -4

            if 400 <= brawler_trophies <= 499:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -3
                rank_9_val = -5
                rank_10_val = -5

            if 500 <= brawler_trophies <= 599:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -6
                rank_10_val = -6

            if 600 <= brawler_trophies <= 699:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -2
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -7
                rank_10_val = -8

            if 700 <= brawler_trophies <= 799:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -5
                rank_9_val = -8
                rank_10_val = -9

            if 800 <= brawler_trophies <= 899:
                rank_1_val = 9
                rank_2_val = 7
                rank_3_val = 5
                rank_4_val = 2
                rank_5_val = 0
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -7
                rank_9_val = -9
                rank_10_val = -10

            if 900 <= brawler_trophies <= 999:
                rank_1_val = 8
                rank_2_val = 6
                rank_3_val = 4
                rank_4_val = 1
                rank_5_val = -1
                rank_6_val = -3
                rank_7_val = -6
                rank_8_val = -8
                rank_9_val = -10
                rank_10_val = -11

            if 1000 <= brawler_trophies <= 1099:
                rank_1_val = 6
                rank_2_val = 5
                rank_3_val = 3
                rank_4_val = 1
                rank_5_val = -2
                rank_6_val = -5
                rank_7_val = -6
                rank_8_val = -9
                rank_9_val = -11
                rank_10_val = -12

            if 1100 <= brawler_trophies <= 1199:
                rank_1_val = 5
                rank_2_val = 4
                rank_3_val = 1
                rank_4_val = 0
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -7
                rank_8_val = -10
                rank_9_val = -12
                rank_10_val = -13

            if brawler_trophies >= 1200:
                rank_1_val = 5
                rank_2_val = 3
                rank_3_val = 0
                rank_4_val = -1
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -8
                rank_8_val = -11
                rank_9_val = -12
                rank_10_val = -13


        if self.player.rank == 1:
            new_trophies = old_tr + rank_1_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_1_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 8
            self.player.resources[0]['Amount'] = old_res_brawl_box + 75
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 2:
            new_trophies = old_tr + rank_2_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_2_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 7
            self.player.resources[0]['Amount'] = old_res_brawl_box + 60
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 3:
            new_trophies = old_tr + rank_3_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_3_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 6
            self.player.resources[0]['Amount'] = old_res_brawl_box + 50
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 4:
            new_trophies = old_tr + rank_4_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_4_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 5
            self.player.resources[0]['Amount'] = old_res_brawl_box + 40
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 5:
            new_trophies = old_tr + rank_5_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_5_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 4
            self.player.resources[0]['Amount'] = old_res_brawl_box + 30
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 6:
            new_trophies = old_tr + rank_6_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_6_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 3
            self.player.resources[0]['Amount'] = old_res_brawl_box + 20
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 7:
            new_trophies = old_tr + rank_7_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_7_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 2
            self.player.resources[0]['Amount'] = old_res_brawl_box + 15
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 8:
            new_trophies = old_tr + rank_8_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_8_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 1
            self.player.resources[0]['Amount'] = old_res_brawl_box + 10
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 9:
            new_trophies = old_tr + rank_9_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_9_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 0
            self.player.resources[0]['Amount'] = old_res_brawl_box + 5
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        elif self.player.rank == 10:
            new_trophies = old_tr + rank_10_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_10_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 0
            self.player.resources[0]['Amount'] = old_res_brawl_box + 0
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(32)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(1)
        self.writeVInt(16)
        self.writeVInt(self.player.home_brawler)
        self.writeVInt(29)
        self.writeVInt(self.player.selected_skins[str(self.player.home_brawler)])
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeString(self.player.name)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(11)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(49)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(35)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(50)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(31)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(51)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(3)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(52)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(26)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(53)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(34)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(54)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(25)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(55)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(8)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(56)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(30)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(57)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(28)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(-1040385)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)