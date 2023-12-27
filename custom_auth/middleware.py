class CookieTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.COOKIES.get('jwt')
        if token is not None:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
        response = self.get_response(request)
        return response