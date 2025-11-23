from django.apps import AppConfig


class PaginasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "paginas"
    
    def ready(self):
        # importa signals para registrar handlers (post_save do User)
        try:
            import paginas.signals  # noqa: F401
        except Exception:
            pass
