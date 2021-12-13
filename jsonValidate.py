from jsonschema import validate

# A sample schema, like what we'd get from json.load()
schema = {
    "type": "string",
    "users": {
        "utilisateurs": {"type": "string"},
        "courrier": {"type": "string"},
        "arrondissement": {"type": "string"},
    },
}


with open("users.json") as f:
    content = f.read()
validate(instance=content, schema=schema)
