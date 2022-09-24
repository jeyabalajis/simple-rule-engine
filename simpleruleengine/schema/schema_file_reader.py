import inspect
import json
import os

import fastjsonschema

from simpleruleengine.utils.type_util import is_dict


class SchemaFileReader:
    def __init__(self, *, schema_file_name_with_path: str):
        self.schema_file_name_with_path = schema_file_name_with_path
        self._schema = {}
        self.__read_schema_file()

    def __read_schema_file(self):
        cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        path = cwd + "/repo/" + self.schema_file_name_with_path + ".json"
        print("cwd: {} path: {}".format(cwd, path))
        with open(self.schema_file_name_with_path) as f:
            self._schema = json.load(f)

    def schema(self):
        return self._schema

    def validate_json_data(self, json_data: dict):
        if not is_dict(json_data):
            raise ValueError("Only Dict allowed")
        return fastjsonschema.compile(self._schema)(json_data)
