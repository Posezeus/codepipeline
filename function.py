import json

def lambda_handler(event, context):
    print("In lambda handler")
    
    print(json.dumps(event))


    return resp