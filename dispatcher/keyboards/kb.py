from pydantic._internal._model_construction import ModelMetaclass


def kb(keyboard: ModelMetaclass, name: str):
    if not keyboard or not name:
        raise ValueError("Keyboard and name must be provided")
    return {name: keyboard}