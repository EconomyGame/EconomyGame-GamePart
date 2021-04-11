import requests

class Api:
    def create_game(self, username):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_lobby/create_game", json={"username": username}).json()
            return {"cfg": d["cfg"], "game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in create_game: " + str(e))
            return {}

    def fetch_game(self, session_token, game_id): #выводит информацию по игре
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/fetch_game", headers={"Authorization":session_token, "Game":game_id}).json()
            return {"game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in fetch_game: " + str(e))
            return {}

    def update_ready(self, session_token, game_id):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/update_ready", headers={"Authorization":session_token, "Game":game_id}).json()
            return {"game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in update_ready: " + str(e))
            return {}

    def leave_game(self, session_token, game_id):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/leave_game", headers={"Authorization":session_token, "Game":game_id}).json()
            return {"game": d["game"]}
        except Exception as e:
            print("exception in leave_game: " + str(e))
            return {}

    def join_game(self, ref_code, username):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/join_game", params={"ref_code":ref_code, "username":username}).json()
            return {"cfg": d["cfg"], "game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in join_game: " + str(e))
            return {}

    def start_game(self, session_token, game_id): #подключение к игре
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/start_game", headers={"Authorization":session_token, "Game":game_id}).json()
            if ("message" in d):
                return False
            else:
                return True
        except Exception as e:
            print("exception in start_game: " + str(e))
            return False

    def get_authorization_data(self, t):
        return (t["user"]["session_token"], t["game"]["_id"])

    def test(self):
        player1 = self.create_game("artemiy")
        player2 = self.join_game(player1["game"]["ref_code"], "artemiy2")
        a1 = self.get_authorization_data(player1)
        a2 = self.get_authorization_data(player2)
        print(self.fetch_game(a1[0], a1[1]))
        print(self.fetch_game(a2[0], a2[1]))
        print(self.update_ready(a1[0], a1[1]))
        print(self.update_ready(a2[0], a2[1]))
        if (self.start_game(a1[0], a1[1])): #без разницы кто из игроков, но только один
            print("YES!")
        else:
            print("NO")
        print(self.leave_game(a1[0], a1[1]))
        print(self.leave_game(a2[0], a2[1]))


