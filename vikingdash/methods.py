def american_time(time : str):
    spliced = time.split(":")
    hour = int(spliced[0])
    if hour > 12:
        hour -= 12
        return f"{hour}:{spliced[1]} PM"
    elif hour == 12:
        return f"{hour}:{spliced[1]} PM"
    else:
        return f"{hour}:{spliced[1]} AM"
    
def alliance_list(alliance : list):
    product = ""
    for team in alliance:
        if team == "6854":
            product += f" <b>{team}</b> -"
        else:
            product += f" {team} -"
    return product.removesuffix(" -")