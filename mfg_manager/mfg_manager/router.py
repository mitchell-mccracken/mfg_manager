from quotes.viewsets import QuoteViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('quotes' , QuoteViewset)