class Presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.populate_table()
        self.view.show()

    def populate_table(self):
        items = self.model.fetch_all_items()
        self.view.populate_table(items)

    def add_item(self, name, firstname):
        self.model.add_item(name, firstname)
        self.populate_table()

    def update_item(self, item_id, new_name):
        self.model.update_item(item_id, new_name)
        self.populate_table()

    def delete_item(self, item_id):
        self.model.delete_item(item_id)
        self.populate_table()