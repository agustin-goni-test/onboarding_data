from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeMeta

def validate_contact_insert_contract(engine, orm_model: DeclarativeMeta):
    '''
    Docstring for validate_contact_insert_contract
    
    :param engine: Description
    :param orm_model: Description
    :type orm_model: DeclarativeMeta
    '''
    # Create inspector to obtain information from actual database engine
    inspector = inspect(engine)

    table = orm_model.__table__
    schema = table.schema
    table_name = table.name

    # Validate schema existence
    if schema not in inspector.get_schema_names():
        raise RuntimeError(f"Schema '{schema}' does not exist in the database.")

    # Validate table existence
    if table_name not in inspector.get_table_names(schema=schema):
        raise RuntimeError(f"Table '{table_name}' does not exist in schema '{schema}'.")

    # Columms
    db_columns = {
        col["name"]: col
        for col in inspector.get_columns(table_name, schema=schema)
    }

    # Validate columns
    for column in table.columns:
        # If column is nullable, skip it (no validation needed)
        if column.nullable:
            continue

        # If necessary column does not exist, raise error
        if column.name not in db_columns:
            raise RuntimeError(
                f"Column '{column.name}' does not exist in table 'contact_info'."
                )
        
        # If necessary column is nullable in DB, raise error
        if db_columns[column.name]["nullable"]:
            raise RuntimeError(
                f"Column '{column.name}' in table '{table_name}' must be NOT NULL."
                )