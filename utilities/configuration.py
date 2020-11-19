import configparser

def Get_API_URL():
    config = configparser.ConfigParser()
    config.read("SDET Training Course/utilities/config.ini")
    return config["API"]["URL"]