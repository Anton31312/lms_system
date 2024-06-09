import re
from rest_framework.serializers import ValidationError


class SiteValidatior:

    def __init__(self, url):
        self.url = url

    def __call__(self, value):
        reg = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$',)
        tmp_url = dict(value).get(self.url)
        if not bool(reg.match(tmp_url)):
            raise ValidationError('Url is not correct. You need used only "youtube.com/*"')