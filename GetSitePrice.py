from GetSiteName import getSiteName


def getSitePrice(siteJSON, fuelJSON, desiredSites):
    FUEL_DICT = {2: "Unleaded", 3: "Diesel", 4: "LPG", 5: "Premium Unleaded 95", 6: "ULSD", 8: "Premium Unleaded 98",
                 11: "LRP", 12: "e10", 13: "Premium e5", 14: "Premium Diesel", 16: "Bio-Diesel 20", 19: "e85",
                 21: "OPAL", 22: "Compressed natural gas", 23: "Liquefied natural gas", 999: "e10/Unleaded",
                 1000: "Diesel/Premium Diesel"}
    desiredFuels = [2]
    fuelPrices = ""
    hasFoundSite = False
    # goes through each site
    for sites in desiredSites:
        hasFoundSite = False
        for site_price in fuelJSON["SitePrices"]:
            # if the site ID matches the desired site
            if site_price["SiteId"] == sites and hasFoundSite is False:
                # gets the name of the site
                fuelPrices = getSiteName(fuelPrices, siteJSON, sites)
                hasFoundSite = True
            for desiredFuel in desiredFuels:
                if site_price["SiteId"] == sites and desiredFuel == site_price["FuelId"]:
                    fuelPrices += FUEL_DICT[site_price["FuelId"]] + ": "
                    fuelPrices += str(site_price["Price"]) + "\n"

    totalPrice = 0
    averagePrice = 0
    count = 0
    for site_price in fuelJSON["SitePrices"]:
        for desiredFuel in desiredFuels:
            if desiredFuel == site_price["FuelId"]:
                totalPrice += site_price["Price"]
                count += 1
    averagePrice = round((totalPrice / count), 2)
    print(averagePrice)
    fuelPrices += "State Average is: " + str(averagePrice)
    return fuelPrices
"""
    for site_price in fuelJSON["SitePrices"]:
        # if the site ID matches the desired site
        if site_price["SiteId"] == desiredSites and hasFoundSite is False:
            # gets the name of the site
            fuelPrices = getSiteName(fuelPrices, siteJSON, desiredSites)
            hasFoundSite = True
        for desiredFuel in desiredFuels:
            if site_price["SiteId"] == desiredSites and desiredFuel == site_price["FuelId"]:
                fuelPrices += FUEL_DICT[site_price["FuelId"]] + ": "
                fuelPrices += str(site_price["Price"]) + "\n"
                hasFoundSite = True
"""
