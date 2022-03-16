import boto3
import logging
import os

sns_client = boto3.client('sns')
SNS_Topic_ARN = os.environ.get('SNS_Topic_ARN')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f'event: {event}')
    
    try:
        ##########################
        ## Your code goes here! ##
        ##########################
        logger.info("StartOutboundCall - Request OK")
        return response
    
    except Exception as error:
        #Log the Error:
        logger.error(error)

        #Send email with error details:
        sns_client.publish(
            TopicArn = SNS_Topic_ARN,
            Subject = 'ERROR: Lambda Request ID {}'.format(context.aws_request_id),
            Message = 
            'Error details: {} \n'.format(error) +
            'More Info: \n' +
            '\n' +
            'Received event: {} \n'.format(f'{event}') +
            'Lambda Request ID: {} \n'.format(context.aws_request_id) +
            'CloudWatch log stream name: {} \n'.format(context.log_stream_name) +
            'CloudWatch log group name: {} \n'.format(context.log_group_name)
            )
        
        #Lambda error response:
        return {
            'statusCode': 400,
            'message': 'An error has occurred',
			'moreInfo': {
				'Lambda Request ID': '{}'.format(context.aws_request_id),
                'CloudWatch log stream name': '{}'.format(context.log_stream_name),
                'CloudWatch log group name': '{}'.format(context.log_group_name)
				}
			}