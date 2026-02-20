import yaml

class ConfigManager:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
            
    def get_api_key(self):
        return self.config['stripe']['api_key']