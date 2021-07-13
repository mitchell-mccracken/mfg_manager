from quotes.viewsets import OpenOrderViewset, QuoteViewset
# from quotes.viewsets import AppUserViewset
# from users.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('quotes' , QuoteViewset)
router.register('openorders' , OpenOrderViewset)
# router.register('users' , UserViewset)      #only if using custom user model
# router.register('appusers' , AppUserViewset)    