from django.apps import AppConfig


class PaperworksConfig(AppConfig):
    name = 'paperworks'

    def ready(self):
        import paperworks.signals