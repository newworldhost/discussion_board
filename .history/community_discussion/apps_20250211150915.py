from django.apps import AppConfig


class CommunityDiscussionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'community_discussion'

def ready(self):
        import community_discussion.signals