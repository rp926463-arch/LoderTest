from loader_test.app.connectors.snowflake_config import SnowflakeConfig
from loader_test.app.connectors.teradata_config import TeradataConfig


class ConnectionFactory:
    @staticmethod
    def create_connection(store, connection_data):
        if "teradata" in store:
            return TeradataConfig(connection_data) if connection_data else None
        elif "snowflake" in store:
            return SnowflakeConfig(connection_data, None, None, None) if connection_data else None
        else:
            raise ValueError("Unknown data store type")
