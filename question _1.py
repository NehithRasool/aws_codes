#Write an AWS Lambda function that adds two numbers and returns the result?


import json

def lambda_handler(event, context):
    try:
        number1 = event.get('number1')
        number2 = event.get('number2')

        if number1 is None or number2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid input: Please provide number1 and number2.')
            }

        result = number1 + number2

        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
