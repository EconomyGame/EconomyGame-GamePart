import requests
import threading
import time


class Api:
    def __init__(self):
        pass


    def _create_game(self, username):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_lobby/create_game",
                              json={"username": username}).json()
            (self.session_token, self.game_id, self.ref_code) = self.get_authorization_data(d)
            return {"cfg": d["cfg"], "game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in _create_game: " + str(e))
            return {}

    def create_game(self, username):
        th = threading.Thread(target=self._create_game, args=(username))
        th.start()
        return

    def _fetch_game(self, session_token, game_id): #выводит информацию по игре
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/fetch_game",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            return {"game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in _fetch_game: " + str(e))
            return {}

    def fetch_game(self):
        th = threading.Thread(target=self._fetch_game, args=(self.session_token, self.game_id))
        th.start()
        return

    def _update_ready(self, session_token, game_id):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/update_ready",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            return {"game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in _update_ready: " + str(e))
            return {}

    def update_ready(self):
        th = threading.Thread(target=self._update_ready, args=(self.session_token, self.game_id))
        th.start()
        return

    def _leave_game(self, session_token, game_id):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/leave_game",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            return {"game": d["game"]}
        except Exception as e:
            print("exception in _leave_game: " + str(e))
            return {}

    def leave_game(self):
        th = threading.Thread(target=self._leave_game, args=(self.session_token, self.game_id))
        th.start()
        return

    def _join_game(self, ref_code, username):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/join_game",
                             params={"ref_code":ref_code, "username":username}).json()
            return {"cfg": d["cfg"], "game": d["game"], "user": d["user"]}
        except Exception as e:
            print("exception in _join_game: " + str(e))
            return {}

    def join_game(self, username):
        th = threading.Thread(target=self._join_game, args=(self.ref_code, username))
        th.start()
        return

    def _start_game(self, session_token, game_id): #подключение к игре
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/start_game",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            if ("message" in d):
                return False
            else:
                return True
        except Exception as e:
            print("exception in _start_game: " + str(e))
            return False

    def start_game(self):
        th = threading.Thread(target=self._start_game, args=(self.session_token, self.game_id))
        th.start()
        return

    def get_authorization_data(self, d):
        return (d["user"]["session_token"], d["game"]["_id"], d["game"]["ref_code"])

    def _make_factory(self, resource_id, coords, session_token, game_id):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/make_factory",
                              json={"resource_id": resource_id, "coords": coords},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            return d
        except Exception as e:
            print("exception in _make_factory: " + str(e))
            return {}

    def make_factory(self, resource_id, coords):
        th = threading.Thread(target=self._make_factory, args=(resource_id, coords, self.session_token, self.game_id))
        th.start()
        return

    def _select_city(self, factory_id, city_id, session_token, game_id):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/select_city",
                              json={"factory_id": factory_id, "city_id": city_id},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            return d
        except Exception as e:
            print("exception in _select_city: " + str(e))
            return {}

    def select_city(self, factory_id, city_id):
        th = threading.Thread(target=self._select_city, args=(factory_id, city_id, self.session_token, self.game_id))
        th.start()
        return

    def _select_source(self, factory_id, source_id, session_token, game_id):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/select_source",
                              json={"factory_id": factory_id, "source_id": source_id},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            return d
        except Exception as e:
            print("exception in _select_source: " + str(e))
            return {}

    def select_source(self, factory_id, source_id):
        th = threading.Thread(target=self._select_source, args=(factory_id, source_id, self.session_token, self.game_id))
        th.start()
        return

    def _upgrade_factory(self, factory_id, session_token, game_id):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/upgrade_factory",
                              json={"factory_id": factory_id},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            return d
        except Exception as e:
            print("exception in _upgrade_factory: " + str(e))
            return {}

    def upgrade_factory(self, factory_id):
        th = threading.Thread(target=self._upgrade_factory, args=(factory_id, self.session_token, self.game_id))
        th.start()
        return

    def test(self):
        player1 = self._create_game("artemiy")
        player2 = self._join_game(player1["game"]["ref_code"], "artemiy2")
        a1 = self.get_authorization_data(player1)
        a2 = self.get_authorization_data(player2)
        print(self._fetch_game(a1[0], a1[1]))
        print(self._fetch_game(a2[0], a2[1]))
        print(self._update_ready(a1[0], a1[1]))
        print(self._update_ready(a2[0], a2[1]))
        if (self._start_game(a1[0], a1[1])): #без разницы кто из игроков, но только один
            print("YES!")
        else:
            print("NO")
        print(self._leave_game(a1[0], a1[1]))
        print(self._leave_game(a2[0], a2[1]))
