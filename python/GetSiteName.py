
def getSiteName(siteJSON, desiredSites):
    # goes through all sites
    for siteNames in siteJSON["S"]:
        # if the desired site is found, return site name
        if siteNames["S"] == desiredSites:
            siteName = siteNames["A"]
            return siteName
