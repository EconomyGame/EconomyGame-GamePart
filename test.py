import requests

ref_code = "Ks8gw"

d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/join_game",
                             params={"ref_code":ref_code, "username":"fake1"}).json()
d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/join_game",
                             params={"ref_code":ref_code, "username":"fake2"}).json()
d = requests.get("http://tp-project2021.herokuapp.com/api/v1/game_lobby/join_game",
                             params={"ref_code":ref_code, "username":"fake3"}).json()