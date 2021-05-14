# AWS-Lambda-Athena

Query AWS Athena using a Lambda Function and store the results in S3

## Table of Contents
* [General Info](#general-info)
* [Setup](#setup)
* [Acknowledgements](#acknowledgements)

## General Info

Built a lambda function to query elb logs I had stored in S3

## Setup

Create an output bucket in S3 where you can store the output from the Lambda Function.
Go into Athena, select settings in the top right corner, and select the output bucket.

This project requires a database and a table.
You can use table already loaded into Athena or you can upload data.
Select 'Connect Data Source' on Athena and select AWS Glue
Go through the steps. Note that you will incur a small charge if you use Glue.
Alternatively you can select 'Create Table', select 'from S3 bucket data', and follow the instructions from there

You must set up permissioning for your Lambda Function.
Set up an IAM Role for Lambda. 
Go ahead and use the [IAM-AthenaLambda.json](https://github.com/GitRubin1/AWS-Lambda-Athena/blob/main/IAM-AthenaLambda.json) policy.
Additionally, assign the 'AmazonS3FullAccess' policy to the role. 

Once you are done, select Python as your interpreter in Lambda.
Edit `QueryString`, `QueryExecutionContext`, and `ResultConfiguration` for your database configuration.

## Acknowledgements

https://www.youtube.com/watch?v=a_Og1t3ULOI as a basis for the project

https://stackoverflow.com/questions/55058618/executing-athena-query-from-python-code-using-boto3-shows-error-botocore-errorf/63023162#63023162?newreg=7af995ec46dd4108b6ecb89c9d4eedca for providing help while troubleshooting

### Note

Input file had IP addresses so not adding that file in the repo

