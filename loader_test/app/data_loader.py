import concurrent.futures
import json

from loader_test.app.data.table_config import TableConfig
from loader_test.app.connectors.snowflake_config import SnowflakeConfig
from loader_test.app.connectors.teradata_config import TeradataConfig


class DataLoader:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            config_data = json.load(file)
            self.tables = {product: [TableConfig(table_data) for table_data in tables] for product, tables in
                           config_data["tables"].items()}
            self.connections = {store: self.create_connection(store, connection_data) for store, connection_data in
                                config_data["connections"].items()}

    def create_connection(self, store, connection_data):
        if "teradata" in store:
            return TeradataConfig(connection_data) if connection_data else None
        elif "snowflake" in store:
            return SnowflakeConfig(connection_data, None, None, None) if connection_data else None
        else:
            raise ValueError("Unknown data store type")

    def loader_execute(self, product, table, control_map):
        kwargs = {
            "load_type": table["load_type"],
            "source_format": "jdbc",
            "source_options": self.connections['teradata'].__dict__,
            "read_opt": "dbTable",
            "source_datastore": table["source_system"],
            "cob_date": table["cob_date"],
            "target_options": self.connections['snowflake'].__dict__
        }
        kwargs["target_options"]["pem_private_key"] = pkb
        kwargs["target_options"]["sfDatabase"] = table["target_database"]
        kwargs["target_options"]["sfSchema"] = table["target_schema"]

        print(kwargs)

    def run(self):
        control_date_map=None
        for product, tables in self.tables.items():
            #print(f"Product: {product}")
            for table in tables:
                #print(table.__dict__)
                executor = concurrent.futures.ThreadPoolExecutor(1)
                executor.submit(self.loader_execute, product, table.__dict__, control_date_map)
                #print(self.connections['snowflake'])


if __name__ == '__main__':
    config = r"../config/appconfig.json"
    obj = DataLoader(config)
    obj.run()
