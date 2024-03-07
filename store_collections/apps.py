from django.apps import AppConfig


class StoreCollectionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_collections'

    def ready(self):
        import store_collections.signals
