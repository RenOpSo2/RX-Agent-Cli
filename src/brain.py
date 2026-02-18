import json
from actions import DISPATCHER

def process_instructions(json_string):
    try:
        data = json.loads(json_string)
        results = []
        
        for action in data.get("actions", []):
            action_type = action.get("type")
            path = action.get("path")
            content = action.get("content", "")

            if action_type in DISPATCHER:
                func = DISPATCHER[action_type]
                if action_type == "create_file":
                    res = func(path, content)
                else:
                    res = func(path)
                results.append(res)
            else:
                results.append(f"Unknown action: {action_type}")
        
        return results
    except Exception as e:
        return [f"Brain Error: {str(e)}"]

