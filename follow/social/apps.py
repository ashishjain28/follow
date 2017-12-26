from django.apps import AppConfig


class SocialConfig(AppConfig):
    name = 'social'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model("Profile"))
        registry.register(self.get_model("Post"))
