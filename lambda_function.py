import json
import boto3
import time


def lambda_handler(event, context):
    client = boto3.client('athena')

    # Setup and perform query
    queryStart = client.start_query_execution(
        QueryString='SELECT elb_name, request_port, backend_port, elb_response_code FROM elb_logs where backend_port = 80 limit 10;',
        QueryExecutionContext={
            'Database': 'sampledb'
        },
        ResultConfiguration={
            'OutputLocation': 's3://athena-results-grubin/'
        }

    )

    # Observe Results
    queryId = queryStart['QueryExecutionId']

    time.sleep(25)

    results = client.get_query_execution(QueryExecutionId=queryId)
    results = client.get_query_results(QueryExecutionId=queryId)
    for row in results['ResultSet']['Rows']:
        print(row)