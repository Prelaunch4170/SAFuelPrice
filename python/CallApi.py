import requests
import json
import os
from GetSitePrice import getSitePrice

def Call_api():
    TOKEN = os.environ['Fuel_API_TOKEN']

    URL_FUEL = "https://fppdirectapi-prod.safuelpricinginformation.com.au/Price/GetSitesPrices?countryId=21" \
               "&geoRegionLevel=3&geoRegionId=4"
    URL_SITE = "https://fppdirectapi-prod.safuelpricinginformation.com.au/Subscriber/GetFullSiteDetails?countryId=" \
               "21&geoRegionLevel=3&geoRegionId=4"

    header = {"Authorization": "FPDAPI SubscriberToken=" + TOKEN,
              "Content-Type": "application/json"}
    # get fuel information for all sites
    responseFuel = requests.get(URL_FUEL, headers=header)
    fuelJSON = responseFuel.json()

    # get site infor to cross referance
    responseSite = requests.get(URL_SITE, headers=header)
    siteJSON = responseSite.json()

    # Replace this with the SiteId you want to filter by
    desiredSiteId = [11111]

    # Filter out the fuel prices for the desired SiteId
    fuelPriceString = getSitePrice(siteJSON, fuelJSON, desiredSiteId)

    return fuelPriceString
