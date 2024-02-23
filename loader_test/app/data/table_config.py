class TableConfig:
    def __init__(self, data):
        self.source_system = data.get("source_system")
        self.target_system = data.get("target_system")
        self.load_type = data.get("load_type")
        self.app_name = data.get("app_name")
        self.cob_date = data.get("cob_date")
        self.source_entity = data.get("source_entity")
        self.target_database = data.get("target_database")
        self.target_table = data.get("target_table")
        self.target_schema = data.get("target_schema")