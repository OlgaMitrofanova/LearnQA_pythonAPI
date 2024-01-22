import json

string_as_json_format = '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}'
obj = json.loads(string_as_json_format)
print(obj['message'])