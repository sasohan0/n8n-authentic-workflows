import sys
import json

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
# Maximum characters to send to AI (Prevents token limit errors)
MAX_CHARS = 2000 

def parse_log(raw_json_string):
    try:
        data = json.loads(raw_json_string)
        
        # 1. Safely extract nested fields (n8n structure varies by version)
        workflow_name = data.get('workflow', {}).get('name', 'Unknown Workflow')
        execution_data = data.get('execution', {})
        error_details = execution_data.get('error', {})
        
        # 2. Get the specific node that failed
        node_name = execution_data.get('lastNodeExecuted', 'Unknown Node')
        
        # 3. Get the Error Message & Stack Trace
        message = error_details.get('message', 'No message provided')
        stack = error_details.get('stack', 'No stack trace')
        
        # 4. Clean and Truncate the Stack Trace
        # We only need the top 5 lines usually
        if stack:
            clean_stack = '\n'.join(stack.split('\n')[:8]) 
        else:
            clean_stack = "No stack trace available."

        # 5. Construct Clean Payload
        clean_data = {
            "workflow_name": workflow_name,
            "node_name": node_name,
            "error_message": message,
            "cleaned_log": f"Error: {message}\nNode: {node_name}\nStack: {clean_stack}"[:MAX_CHARS]
        }
        
        return clean_data

    except Exception as e:
        # Fallback if parsing fails totally
        return {
            "workflow_name": "Log Parser Failed",
            "node_name": "Script Error",
            "error_message": str(e),
            "cleaned_log": f"Could not parse error log. Raw error: {str(e)}"
        }

if __name__ == "__main__":
    # Input comes from command line argument
    if len(sys.argv) > 1:
        raw_input = sys.argv[1]
        result = parse_log(raw_input)
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "No input provided to script"}))