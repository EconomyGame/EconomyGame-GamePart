class City:

    def __init__(self, _id, x, y, name, resource_delta, resource_levels, resource_stage):
        self._id = _id
        self.x = x
        self.y = y
        self.name = name
        self.resource_delta = resource_delta
        self.resource_levels = resource_levels
        self.resource_stage = resource_stage


class Factory:

    def __init__(self, _id, x, y, city_id, coef, level, resource_id, source_id, username):
        self._id = _id
        self.x = x
        self.y = y
        self.city_id = city_id
        self.coef = coef
        self.level = level
        self.resource_id = resource_id
        self.source_id = source_id
        self.username = username


class Source:

    def __init__(self, _id, x, y, delta, remain, res_id):
        self._id = _id
        self.x = x
        self.y = y
        self.delta = delta
        self.remain = remain
        self.res_id = res_id
