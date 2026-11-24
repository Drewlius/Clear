import configparser

def create_config():
    config = configparser.ConfigParser()
    config['Model'] = {
        "model" : input("ModelID"),
        "provider": input("Provider"),
        "baseURL": input("BaseURL with http://"),
        "apiKey": input("apiKey")
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    model = config.get('Model', 'model')
    provider = config.get('Model', 'provider')
    baseURL = config.get('Model', 'baseURL')
    apiKey = config.get('Model', 'apiKey')

    config_values = {
        'model': model,
        'provider': provider, 
        'baseURL': baseURL,
        'apiKey': apiKey
    }

    return config_values

if __name__ == "__main__":
    create_config()
    