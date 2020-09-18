import configparser

config = configparser.ConfigParser()
config.read('./common/configinfo.ini')
print(config['DEFAULT']['platformName'])
# ss="济南市市中区"
# print(ss[0:2])