import inspect
import json
import os

import fastjsonschema

from simpleruleengine.utils.type_util import is_dict


class SchemaReader:
    def __init__(self, *, schema_file_name: str):
        self.schema_file_name = schema_file_name
        self._schema = {}
        self.__read_schema_file()

    def __read_schema_file(self):
        cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        path = cwd + "/repo/" + self.schema_file_name + ".json"
        with open(path) as f:
            self._schema = json.load(f)

    def schema(self):
        return self._schema

    def validate_json_data(self, json_data: dict):
        if not is_dict(json_data):
            raise ValueError("Only Dict allowed")
        return fastjsonschema.compile(self._schema)(json_data)
