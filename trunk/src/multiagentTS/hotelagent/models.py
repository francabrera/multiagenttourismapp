from django.db import models

# Create your models here.
'''
      <hotel>
        <price url="/book/hotel?code=1-l_qOlD5EqKFusVVrbHAI.SpHFiPitTNBu4MGtOIOs.5-uTe8xW1P9WEEhLkBUrQ.H.WRIHOSTELS.2225.125734&amp;_sid_=5-uTe8xW1P9WEEhLkBUrQ" currency="USD">22</price>
        <pricehistorylo>0.00</pricehistorylo>
        <pricehistoryhi>0.00</pricehistoryhi>
        <stars>0.0</stars>
        <name>YMCA of Greater Boston</name>
        <phone></phone>
        <address>316 Huntington Avenue</address>
        <city>Boston</city>
      </hotel>
'''
'''
'' Clase que gestiona un hotel
'''
class HotelModel(models.Model):
    price = models.CharField(max_length = 50)
    moneda = models.CharField(max_length = 10)
    stars = models.CharField(max_length = 3)
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    
    def __init__(self, hotel):
        models.Model.__init__(self)
        self.price = hotel.findtext('price')
        self.moneda = hotel.find('price').attrib['currency']
        self.stars = hotel.findtext('stars')
        self.name = hotel.findtext('name')
        self.phone = hotel.findtext('phone')
        self.address = hotel.findtext('address')
        self.city = hotel.findtext('city')
