# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')


# from pprint import pprint
# acm_client = session.client('acm', region_name='us-east-1')
# paginator = acm_client.get_paginator('list_certificates')
# for page in paginator.paginate(CertificateStatuses=['ISSUED']):
#     for cert in page['CertificateSummaryList']:
#         pprint(cert)
