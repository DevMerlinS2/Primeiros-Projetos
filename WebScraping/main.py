from web_scraping import *

url = "https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&category=MLB5726&fulfillment=1#deal_print_id=06a55050-e173-11ee-a541-5b01347c354d&c_id=carousel&c_element_order=2&c_campaign=BOLOTA_ENTREGA_RAPIDA&c_uid=06a55050-e173-11ee-a541-5b01347c354d"
web_scraping = webScraping(url)
print(web_scraping.pick_all_rooms())