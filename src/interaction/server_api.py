import requests
import threading


class Api:

    def __init__(self, game):
        self.game = game
        self.session_token = dict()
        self.game_id = None
        self.ref_code = None

    def _create_game(self, username, callback):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_lobby/create_game",
                              json={"username": username}).json()
            self.session_token[username], self.game_id, self.ref_code = self.get_authorization_data(d)
            # api = {"cfg": d["cfg"], "game": d["game"], "user": d["user"]}
            self.game.handle_update(d)
            callback(d)
            return d
        except Exception as e:
            print("exception in _create_game: " + str(e))
            return {}

    def create_game(self, username, callback=lambda x: None):
        th = threading.Thread(target=self._create_game,
                              args=(username, callback))
        th.start()
        return

    def _fetch_game(self, session_token, game_id, callback): #выводит информацию по игре
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/fetch_game",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            api = {"game": d["game"], "user": d["user"]}
            self.game.handle_update(api)
            callback(api)
            return api
        except Exception as e:
            print("exception in _fetch_game: " + str(e))
            return {}

    def fetch_game(self, username, callback=lambda x: None):
        th = threading.Thread(target=self._fetch_game,
                              args=(self.session_token[username], self.game_id, callback))
        th.start()
        return

    def _update_ready(self, session_token, game_id, callback):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/update_ready",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            api = {"game": d["game"], "user": d["user"]}
            self.game.handle_update(api)
            callback(api)
            return api
        except Exception as e:
            print("exception in _update_ready: " + str(e))
            return {}

    def update_ready(self, username, callback=lambda x: None):
        th = threading.Thread(target=self._update_ready,
                              args=(self.session_token[username], self.game_id, callback))
        th.start()
        return

    def _leave_game(self, session_token, game_id, callback):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/leave_game",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            api = {"game": d["game"]}
            self.game.handle_update(api)
            callback(api)
            return api
        except Exception as e:
            print("exception in _leave_game: " + str(e))
            return {}

    def leave_game(self, username, callback=lambda x: None):
        th = threading.Thread(target=self._leave_game,
                              args=(self.session_token[username], self.game_id, callback))
        th.start()
        return

    def _join_game(self, ref_code, username, callback):
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/join_game",
                             params={"ref_code":ref_code, "username":username}).json()
            self.session_token[username] = d["user"]["session_token"]
            self.game_id, self.ref_code = d["game"]["_id"], ref_code
            api = {"cfg": d["cfg"], "game": d["game"], "user": d["user"]}
            self.game.handle_update(api)
            callback(api)
            return api
        except Exception as e:
            print("exception in _join_game: " + str(e))
            return {}

    def join_game(self, username, ref_code, callback=lambda x: None):
        th = threading.Thread(target=self._join_game,
                              args=(ref_code, username, callback))
        th.start()
        return

    def _start_game(self, session_token, game_id, callback): #подключение к игре
        try:
            d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/start_game",
                             headers={"Authorization":session_token, "Game":game_id}).json()
            api = d
            if ("message" in d):
                callback((False, api))
                return (False, api)
            else:
                callback((True, api))
                self.test_city_id = api["game"]["cities"][0]["_id"]
                self.test_source_id = api["game"]["sources"][0]["_id"]
                return (True, api)
        except Exception as e:
            print("exception in _start_game: " + str(e))
            return False

    def start_game(self, username, callback=lambda x: None):
        th = threading.Thread(target=self._start_game,
                              args=(self.session_token[username], self.game_id, callback))
        th.start()
        return

    def get_authorization_data(self, d):
        return (d["user"]["session_token"], d["game"]["_id"], d["game"]["ref_code"])

    def _make_factory(self, resource_id, coords, session_token, game_id, callback):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/make_factory",
                              json={"resource_id": resource_id, "coords": coords},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            api = d
            callback(api)
            return api
        except Exception as e:
            print("exception in _make_factory: " + str(e))
            return {}

    def make_factory(self, username, resource_id, coords, callback=lambda x: None): #ID ресурса, в диапазоне [1, 4], Координаты расположения фабрики
        th = threading.Thread(target=self._make_factory,
                              args=(resource_id, coords, self.session_token[username], self.game_id, callback))
        th.start()
        return

    def _select_city(self, factory_id, city_id, session_token, game_id, callback): #соединение фабрики и города
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/select_city",
                              json={"factory_id": factory_id, "city_id": city_id},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            api = d
            callback(api)
            return api
        except Exception as e:
            print("exception in _select_city: " + str(e))
            return {}

    def select_city(self, username, factory_id, city_id, callback=lambda x: None):
        th = threading.Thread(target=self._select_city,
                              args=(factory_id, city_id, self.session_token[username], self.game_id, callback))
        th.start()
        return

    def _select_source(self, factory_id, source_id, session_token, game_id, callback):
        try:
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/select_source",
                              json={"factory_id": factory_id, "source_id": source_id},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            api = d
            callback(api)
            return api
        except Exception as e:
            print("exception in _select_source: " + str(e))
            return {}

    def select_source(self, username, factory_id, source_id, callback=lambda x: None):
        th = threading.Thread(target=self._select_source,
                              args=(factory_id, source_id, self.session_token[username], self.game_id, callback))
        th.start()
        return

    def _upgrade_factory(self, factory_id, session_token, game_id, callback):
        try:
            print(factory_id, session_token, game_id)
            d = requests.post("http://tp-project2021.herokuapp.com/api/v1/game_factories/upgrade_factory",
                              json={"factory_id": factory_id},
                              headers={"Authorization":session_token, "Game":game_id}).json()
            api = d
            print(api)
            callback(api)
            return api
        except Exception as e:
            print("exception in _upgrade_factory: " + str(e))
            return {}

    def upgrade_factory(self, username, factory_id, callback=lambda x: None):
        th = threading.Thread(target=self._upgrade_factory,
                              args=(factory_id, self.session_token[username], self.game_id, callback))
        th.start()
        return

    def cb(self, api):
        print(api)

    def cb_start_game(self, api):
        if (api[0]): #без разницы кто из игроков, но только один
            print("YES!")
        else:
            print("NO")

    def test(self):
        #Для тестирования во все функции был добален join, а также были добавлены test_factory_id, test_city_id, test_source_id
        self.create_game("artemiy", self.cb)
        print("create!")
        self.join_game("artemiy2", self.cb)
        print("join!")
        self.fetch_game("artemiy", self.cb)
        print("fetch!")
        self.update_ready("artemiy", self.cb)
        self.update_ready("artemiy2", self.cb)
        print("update!")
        self.start_game("artemiy", self.cb_start_game) #можно запускать игру на ком угодно
        print("start or no")
        self.make_factory("artemiy", 1, [1, 1], self.cb) #уровень фабрики и координаты
        print("make_factory!")
        self.select_city("artemiy", self.test_factory_id, self.test_city_id, self.cb) #factory_id, city_id соединяем их
        print("select_city!")
        self.select_source("artemiy", self.test_factory_id, self.test_source_id, self.cb) #factory_id, source_id соединяем их
        print("select_source!")
        self.upgrade_factory("artemiy", self.test_factory_id, self.cb) #factory_id
        print("upgrade_factory!")
        self.leave_game("artemiy", self.cb)
        self.leave_game("artemiy2", self.cb)
        print("leave_game!")

#Api().test()
