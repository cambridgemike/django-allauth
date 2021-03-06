from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class VKAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('link')

    def get_avatar_url(self):
        ret = None
        photo_big_url = self.account.extra_data.get('photo_big')
        photo_medium_url = self.account.extra_data.get('photo_medium')
        if photo_big_url:
            return photo_big_url
        elif photo_medium_url:
            return photo_medium_url
        else:
            return ret

    def to_str(self):
        dflt = super(VKAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class VKProvider(OAuth2Provider):
    id = 'vk'
    name = 'VK'
    package = 'allauth.socialaccount.providers.vk'
    account_class = VKAccount

    def extract_uid(self, data):
        return str(data['uid'])

    def extract_common_fields(self, data):
        return dict(last_name=data.get('last_name'),
                    username=data.get('screen_name'),
                    first_name=data.get('first_name'))


providers.registry.register(VKProvider)
