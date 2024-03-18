from bs4 import BeautifulSoup
import requests

class webScraping:
    def __init__(self, url):
         self.url = url
         self.soup = self.getHTML()

    def getHTML(self):
         req = requests.get(self.url)
         soup = BeautifulSoup(req.content, 'html.parser')
         return soup
    
    def get_Rooms(self):
        return self.soup.find_all('div', class_='promotion-item__description')
    
    def get_title(self, room):
        return room.find('p', class_='promotion-item__title').text

    def get_entrega(self, room):
        return room.find('div', class_= 'promotion-item__newshipping-container').find('span', class_='promotion-item__pill').text
    
    def get_price(self, room):
        return room.find('div', class_= 'andes-money-amount-combo__main-container').find('span', class_= 'andes-money-amount__fraction').text


    def pick_all_rooms(self):
        list_rooms = []
        for room in self.get_Rooms():
            room_dicionario = {}
            room_dicionario['Titulo'] = self.get_title(room)
            room_dicionario['Entrega'] = self.get_entrega(room)
            room_dicionario['Preço'] = self.get_price(room)
            list_rooms.append(room_dicionario)
        return list_rooms