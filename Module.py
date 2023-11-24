class Module:
    def __init__(self, token, name, professors):
        self._token = token
        self._name = name
        self._professors = professors

    def get_number(self): return self._token

    def get_name(self): return self._name

    def get_professors(self): return self._professors

    def __str__(self): return self._name
