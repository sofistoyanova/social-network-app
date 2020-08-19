from users_app.models import UserVisits

class TrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip_address = request.META.get('REMOTE_ADDR')

        response = self.get_response(request)

        session_key = request.session.session_key
        user = UserVisits.objects.filter(session_key=session_key)

        if not user:
            try:
                if request.user.is_authenticated:
                    UserVisits.objects.create(user=request.user, ip_address=client_ip_address, session_key=session_key)
            except:
                pass
        return response
