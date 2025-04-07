from typing import Any


class adict(dict):
    """
    Simple dot access dictionary. Supports recursion.
    """

    def __init__(self, *args, **kwargs):
        super(adict, self).__init__(*args, **kwargs)
        for __name, __value in self.items():
            self.__setattr__(__name, __value)

    def __getattr__(self, __name: str) -> Any:
        try:
            return self[__name]
        except KeyError:
            # raise AttributeError(__name)
            return None

    def __setattr__(self, __name: str, __value: Any) -> None:
        if isinstance(__value, dict):
            self[__name] = self.__class__(__value)
        else:
            self[__name] = __value
        # this appends attribute to the class
        object.__setattr__(self, __name, __value)

    def __delattr__(self, __name: str) -> None:
        if __name in self:
            del self[__name]

    def __getstate__(self):
        return dict(self.__dict__)

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(%s)" % ", ".join([
            f"{__name}={__value}" for __name, __value in self.items()
        ])
