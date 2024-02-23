class TeradataConfig:
    def __init__(self, data):
        self.logmech = data.get("logmech")
        self.url = data.get("url")
        self.driver = data.get("driver")
        self.keytabs = data.get("keytabs")
        self.principal = data.get("principal")
        self.encryptdata = data.get("encryptdata")
        self.refreshKrb5Config = data.get("refreshKrb5Config")