import json

def generate_vscode_snippet(filename, prefix,description):
    with open(filename, 'r',encoding='utf-8') as file:
        code = file.read()
    
    snippet = {
        "prefix": prefix,
        "body": code.splitlines(),
        "description": description
    }

    return json.dumps(snippet, indent=2)


if __name__ == "__main__":
    filename = "best-template.py"
    prefix = "acm"
    description = "ACM模板"
    snippet_config = generate_vscode_snippet(filename, prefix,description)
    with open("acm.json", 'w',encoding='utf-8') as file:
        file.write(snippet_config)