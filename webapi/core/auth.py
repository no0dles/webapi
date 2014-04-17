from webapi.http.response import UnauthorizedResponse


def requires_auth():
    def wrap(f):
        def wrapped_f(*args):
            try:
                if args[1].user:
                    return f(*args)
            except:
                pass

            return UnauthorizedResponse()
        return wrapped_f
    return wrap


def allowed_roles(roles=[]):
    def wrap(f):
        def wrapped_f(*args):
            try:
                for r in roles:
                    if r in args[1].roles:
                        return f(*args)
            except:
                pass

            return UnauthorizedResponse()
        return wrapped_f
    return wrap


def allowed_users(users=[]):
    def wrap(f):
        def wrapped_f(*args):
            try:
                if len(users) > 0 and args[1].user in users:
                    return f(*args)
            except:
                pass

            return UnauthorizedResponse()
        return wrapped_f
    return wrap