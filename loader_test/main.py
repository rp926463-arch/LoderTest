from loader_test.app.data_loader import DataLoader

config = DataLoader("./config/appconfig.json")


for product, tables in config.tables.items():
    print(f"Product: {product}")
    for table in tables:
        print(table.__dict__)


for data_store, connection_info in config.connections.items():
    print(f"({data_store})")
    print(f"{connection_info.__dict__}")

# print(f"Snowflake Connection URL: {config.connections['snowflake'].sfUrl}")
# print(f"Snowflake Warehouse: {config.connections['snowflake'].sfWarehouse}")
