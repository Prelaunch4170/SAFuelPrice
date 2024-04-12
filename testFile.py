from GetSiteName import getSiteName


def getSitePrice(siteJSON, fuelJSON, desiredSites):
    FUEL_DICT = {2: "Unleaded", 3: "Diesel", 4: "LPG", 5: "Premium Unleaded 95", 6: "ULSD", 8: "Premium Unleaded 98",
                 11: "LRP", 12: "e10", 13: "Premium e5", 14: "Premium Diesel", 16: "Bio-Diesel 20", 19: "e85",
                 21: "OPAL", 22: "Compressed natural gas", 23: "Liquefied natural gas", 999: "e10/Unleaded",
                 1000: "Diesel/Premium Diesel"}
    desiredFuels = [2, 3, 4]
    fuelPrices = ""
    siteNames = {}
    hasFoundSite = False
    # goes through each site
    for site_price in fuelJSON["SitePrices"]:
        # if the site ID matches the desired site
        lookingVariable = site_price["SiteId"]
        for Site in desiredSites:
            if site_price["SiteId"] == Site and hasFoundSite is False:
                # gets the name of the site
                fuelPrices = getSiteName(fuelPrices, siteJSON, Site)
                hasFoundSite = True
        for desiredFuel in desiredFuels:
            if site_price["SiteId"] == Site and desiredFuel == site_price["FuelId"]:
                fuelPrices += FUEL_DICT[site_price["FuelId"]] + ":"
                fuelPrices += str(site_price["Price"]) + "\n"
            hasFoundSite = False

    return fuelPrices
