import requests
import json
import os



def Call_api():
    TOKEN = os.environ['Fuel_API_TOKEN']
    fuel_dict = {2: "Unleaded", 3: "Diesel", 4: "LPG", 5: "Premium Unleaded 95", 6: "ULSD", 8: "Premium Unleaded 98",
                 11: "LRP", 12: "e10", 13: "Premium e5", 14: "Premium Diesel", 16: "Bio-Diesel 20", 19: "e85",
                 21: "OPAL", 22: "Compressed natural gas", 23: "Liquefied natural gas", 999: "e10/Unleaded",
                 1000: "Diesel/Premium Diesel"}

    URL = "https://fppdirectapi-prod.safuelpricinginformation.com.au/Price/GetSitesPrices?countryId=21&geoRegionLevel=3" \
          "&geoRegionId=4"
    header = {"Authorization": "FPDAPI SubscriberToken=" + TOKEN,
              "Content-Type": "application/json"}

    response = requests.get(URL, headers=header)
    usable = response.json()

    # Replace this with the SiteId you want to filter by
    desired_site_id = 61577374

    # Filter out the fuel prices for the desired SiteId
    fuel_prices = ''

    desired_Fuel = 2
    for site_price in usable["SitePrices"]:
        if site_price["SiteId"] == desired_site_id:
            if desired_Fuel == site_price["FuelId"]:
                fuel_prices += "The price for " + str(site_price["SiteId"]) + " is: \n"
                fuel_prices += fuel_dict[site_price["FuelId"]] + ": "
                fuel_prices += str(site_price["Price"])

    return fuel_prices
