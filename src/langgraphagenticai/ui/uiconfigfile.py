from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)
        
    def get_llm_options(self):
        ## how will it read the LLM options
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")