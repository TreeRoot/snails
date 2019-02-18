# -*- coding:utf-8 -*- 


class point_dict(dict):
    """
        字典点属性访问
    """

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            # raise AttributeError(name)
            return None

    def __setattr__(self, name, value):
        self[name] = value
