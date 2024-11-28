import reflex as rx

class TestModel(rx.Model, table=True):
    id: str
    name: str