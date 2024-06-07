import re
from rest_framework.serializers import ValidationError


class SiteValidatior:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value in ['youtube.com']:
            raise ValidationError('Url is not correct. You need used only "youtube.com/*"')