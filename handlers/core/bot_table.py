from typing import List, Dict, Union

from prettytable import PrettyTable

from api.sheets import GetRecords
from config.sheets import Columns


default_columns: List[str] = [
    Columns.PLAYER_NAME.value,
    Columns.ANSWER.value,
]


class TableConfig:
    def __init__(self, fields: List[str] = default_columns):
        self.fields = fields
        self.table = PrettyTable(fields)

    def prepare_data_from_sheet(
            self,
            data: List[Dict[str, Union[int, float, str]]],
            col_names: List[str]
    ) -> List[List[str]]:
        processed = []
        for item in data:
            user_data = []
            for column in col_names:
                formatted_text = item.get(column).replace(', ', '\n')
                user_data.append(formatted_text)
            processed.append(user_data)
        return processed


class TableBuilder(TableConfig):
    def build_rows(self, rows: List[List[str]]):
        for row in rows:
            self.table.add_row(row)


class TableView:
    def __init__(self, fields: List[str] = default_columns):
        self.table_builder = TableBuilder(fields)
        self.get_records = GetRecords()

    def show_by_rows(self) -> PrettyTable:
        records = self.get_records.get_all_records()
        prepared_data = self.table_builder.prepare_data_from_sheet(records, self.table_builder.fields)
        self.table_builder.build_rows(prepared_data)
        return self.table_builder.table
