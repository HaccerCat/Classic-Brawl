from ByteStream.Writer import Writer

class BattleResult2Message(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.db = db



    def encode(self):
        self.writeVInt(1)
        self.writeVInt(self.player.battle_result)
        #self.writeVInt(8) high probability to remove, it was just for testing trophies gained
        #somehow the match became power play

        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        old_tr = self.player.trophies


        if 0 <= brawler_trophies <= 49:
            win_val = 8
            lose_val = 0

        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 8
                lose_val = -1

            if 100 <= brawler_trophies <= 199:
                win_val = 8
                lose_val = -2

            if 200 <= brawler_trophies <= 299:
                win_val = 8
                lose_val = -3

            if 300 <= brawler_trophies <= 399:
                win_val = 8
                lose_val = -4

            if 400 <= brawler_trophies <= 499:
                win_val = 8
                lose_val = -5

            if 500 <= brawler_trophies <= 599:
                win_val = 8
                lose_val = -6

            if 600 <= brawler_trophies <= 699:
                win_val = 8
                lose_val = -7

            if 700 <= brawler_trophies <= 799:
                win_val = 8
                lose_val = -8

            if 800 <= brawler_trophies <= 899:
                win_val = 7
                lose_val = -9

            if 900 <= brawler_trophies <= 999:
                win_val = 6
                lose_val = -10

            if 1000 <= brawler_trophies <= 1099:
                win_val = 5
                lose_val = -11

            if 1100 <= brawler_trophies <= 1199:
                win_val = 4
                lose_val = -12

            if brawler_trophies >= 1200:
                win_val = 3
                lose_val = -12

        if self.player.battle_result == 0:
            new_trophies = old_tr + win_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + win_val
            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 5
            self.player.resources[0]['Amount'] = old_res_brawl_box + 50
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)
        else:
            new_trophies = old_tr + lose_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + lose_val
            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            old_res_brawl_box = self.player.resources[0]['Amount']
            old_res_big_box = self.player.resources[2]['Amount']
            self.player.resources[2]['Amount'] = old_res_big_box + 5
            self.player.resources[0]['Amount'] = old_res_brawl_box + 25
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
        self.writeVInt(6)
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
        self.writeVInt(0)
        self.writeVInt(16)
        self.writeVInt(self.player.bot1)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)

        self.writeString(self.player.bot1_n)

        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(0)
        self.writeVInt(16)
        self.writeVInt(self.player.bot2)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)

        self.writeString(self.player.bot2_n)

        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(self.player.bot3)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)

        self.writeString(self.player.bot3_n)

        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(self.player.bot4)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)

        self.writeString(self.player.bot4_n)

        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(2)
        self.writeVInt(16)
        self.writeVInt(self.player.bot5)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeVInt(0)

        self.writeString(self.player.bot5_n)

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