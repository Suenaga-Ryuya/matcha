import json

a = [
    "comment",
    "constant",
    "entity",
    "invalid",
    "keyword",
    "markup",
    "meta",
    "punctuation",
    "source",
    "storage",
    "string",
    "support",
    "text",
    "variable"
]

json_array = []

for i in a:
    json_array.append(
        {
            "name": i,
            "scope": [
                i
            ],
            "settings": {
                "foreground": "#FCFCFC"
            }
        }
    )

with open('token.json', 'w') as f:
    json.dump(json_array, f, indent=4, sort_keys=True)