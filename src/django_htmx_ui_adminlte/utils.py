from hashlib import md5


def avatar_url(user):
    if user.is_anonymous:
        return 'https://www.gravatar.com/avatar/%s?s=80&d=mp' % md5('anonymous'.encode('utf-8')).hexdigest()
    if hasattr(user, 'profile') and user.profile.avatar:
        return user.profile.avatar.url
    if hasattr(user, 'socialaccount_set'):
        social_accounts = user.socialaccount_set.all()
        if social_accounts:
            for a in social_accounts:
                avatar = a.get_avatar_url()
                if avatar:
                    return avatar
    return 'https://www.gravatar.com/avatar/%s?s=80&d=mp' % md5(user.email.encode('utf-8')).hexdigest()
