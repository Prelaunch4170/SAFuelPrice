
def getSiteName(siteName, siteJSON, desiredSites):
    # goes through all sites
    for siteNames in siteJSON["S"]:
        # if the desired site is found, return site name
        if siteNames["S"] == desiredSites:
            siteName += "The price for " + siteNames["A"] + " is: \n"
            return siteName
