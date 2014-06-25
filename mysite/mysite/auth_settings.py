TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth',
)

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

AUTHENTICATION_BACKENDS = ('social.backends.vk.VKOAuth2',
                           'django.contrib.auth.backends.ModelBackend',)
VK_APP_ID = '4431663'
VK_API_SECRET = 'srIvtyCHUvOxRANl3Ef0'

