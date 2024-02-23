class SnowflakeConfig:
    def __init__(self, data, pkb=None, sf_table=None, sf_schema=None):
        self.sfUrl = data.get("sfUrl")
        self.sfAccount = data.get("sfAccount")
        self.sfUser = data.get("sfUser")
        self.pem_private_key = pkb
        self.sfRole = data.get("sfRole")
        self.sfWarehouse = data.get("sfWarehouse")
        self.sfTable = sf_table
        self.sfSchema = sf_schema
