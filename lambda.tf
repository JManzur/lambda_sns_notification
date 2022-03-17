/* Lambda Function with SNS Notification */

# Zip the lambda code
data "archive_file" "init" {
  type        = "zip"
  source_dir  = "lambda_code/"
  output_path = "output_lambda_zip/lambda_sns_notification.zip"
}

# Create lambda function
resource "aws_lambda_function" "lambda_sns_notification" {
  filename      = data.archive_file.init.output_path
  function_name = "Lambda_SNS_Notification"
  role          = aws_iam_role.LambdaSNS_policy_role.arn
  handler       = "main_handler.lambda_handler"
  description   = "Lambda with SNS Notification"
  tags          = merge(var.project-tags, { Name = "${var.resource-name-tag}-lambda" })

  # Prevent lambda recreation
  source_code_hash = filebase64sha256(data.archive_file.init.output_path)

  runtime = "python3.9"
  timeout = "120"

  environment {
    variables = {
      SNS_Topic_ARN = aws_sns_topic.Error_Notification.arn
    }
  }

  depends_on = [
    aws_sns_topic.Error_Notification
  ]
}