import requests
from bs4 import BeautifulSoup
import smtplib

world_URL = 'https://www.worldometers.info/coronavirus/'

Canada_URL = 'https://www.worldometers.info/coronavirus/country/canada/' #Can add any country of choice


class track:
    def __init__(self, URL):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        #Total count scraping
        total_span = soup.find('div', {'class': 'maincounter-number'})
        self.total_count = total_span.findChildren('span')[0].text

        #Total deaths scraping
        deaths_span = soup.find_all('div', {'class': 'maincounter-number'})[1]
        self.total_deaths = deaths_span.findChildren('span')[0].text


World = track(world_URL)

Canada = track(Canada_URL)

#Mailing function
def mail():
    server = smtplib.SMTP('smtp.gmail.com', 587) #For gmail
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', '') #The user login information will be required

    subject = 'World and Canada COVID-19 Cases'

    body = 'As of today Worldwide: \
            \nTotal Cases: ' + World.total_count + '\
            \nTotal Deaths: ' + World.total_deaths + '\
            \n\nAs of today in Canada: \
            \nTotal Cases: ' + Canada.total_count + '\
            \nTotal Deaths: ' + Canada.total_deaths + '\
            \n\nFor more statistics visit: https://www.worldometers.info/coronavirus/'

    message = f"Subject: {subject}\n\n{body}"


    server.sendmail(
        '', #Email sender 
        '',
        message #Email reciever (Can be the same as the sender - it will just be a mail to the same person)
    )

    print("Email Sent!")

    server.quit()


mail()

