from django.apps import AppConfig


class CommunityDiscussionConfig(AppConfig):
    """
    Configuration class for the Community Discussion app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'community_discussion'

    def ready(self):
        """
        Import signals when the app is ready.
        """
        import community_discussion.signals