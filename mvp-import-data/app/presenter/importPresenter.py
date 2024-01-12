from ..common.importThread import ImportThread

class ImportPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.start_import_signal.connect(self.start_import)

    def start_import(self):
        self.view.reset_progress_bar()
        self.model.set_data(self.view.generate_dummy_data())
        self.import_thread = ImportThread(self.model)
        self.import_thread.update_progress.connect(self.view.update_progress_bar)
        self.import_thread.start()
