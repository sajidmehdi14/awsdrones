#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Webotron Deploy websites with AWS.

Webotron automtes the process of deploying static websites on aws.
- Configure AWS S3 Buckets
 - Create them
 - Set them up for static websites hosting
 - Deploy local files to them (S3)
- Configure DNS with Route 53
- Configure a Content Delivery Network and SSL with AWS CloudFront
"""

import boto3
import botocore
import click
import util
from bucket import BucketManager
from domain import DomainManager
from certificate import CertificateManager
from cdn import DistributionManager


session = None
bucket_manager = None
domain_manager = None
cert_manager = None
dist_manager = None
# s3 = session.resource('s3')


@click.group()
@click.option('--profile',default=None,
        help="Use a given AWS profile.")
def cli(profile):
    """Webotron deploys websites to AWS."""
    global session, bucket_manager, domain_manager, cert_manager, dist_manager

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)
    bucket_manager = BucketManager(session)
    domain_manager = DomainManager(session)
    cert_manager = CertificateManager(session)
    dist_manager = DistributionManager(session)


@cli.command('list-buckets')
def list_buckets():
    """List all s3 Buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bicket_objects(bucket):
    """List objects in an s3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to Bucket."""
    bucket_manager.sync(pathname, bucket)
    print(bucket_manager.get_bucket_url(bucket_manager.s3.Bucket(bucket)))

# @cli.command('setup-domain')
# @click.argument('domain')
# def setup_domain(domain):
#     """Configure DOMAIN to point to BUCKET."""
#     bucket = bucket_manager.get_bucket(domain)
#     zone = DomainManager(session).find_hosted_zone(domain)
#     print(zone)

# Route 53 (zone ID) Z02674283FXKHIDDU48JQ
@cli.command('setup-domain')
@click.argument('domain')
def setup_domain(domain):
    """Configure DOMAIN to point to BUCKET."""
    bucket = bucket_manager.get_bucket(domain)
    # zone = DomainManager(session).create_hosted_zone(domain)
    # print(zone)
    # r53 = boto3.client('route53')
    # zones = r53.list_hosted_zones(bucket=domain)
    # if not zones or len(zones['HostedZones']) == 0:
    #     raise Exception("Could not find DNS zone to update")
    # zone_id = zones['HostedZones'][0]['Id']
    # print(zone_id)
    endpoint = util.get_endpoint(bucket_manager.get_region_name(bucket))
    DomainManager(session).create_s3_domain_record('Z02674283FXKHIDDU48JQ', domain, endpoint)
    print("Domain configured: http://{}".format(domain))


@cli.command('find-cert')
@click.argument('domain')
def find_cert(domain):
    """Find a certificate for <DOMAIN>."""
    print(cert_manager.find_matching_cert(domain))


@cli.command('setup-cdn')
@click.argument('domain')
@click.argument('bucket')
def setup_cdn(domain, bucket):
    """Set up CloudFront CDN for DOMAIN pointing to BUCKET."""
    dist = dist_manager.find_matching_dist(domain)

    if not dist:
        cert = cert_manager.find_matching_cert(domain)
        # print("1- ######################")
        # print(cert)
        if not cert:  # SSL is not optional at this time
            print("Error: No matching cert found.")
            return

        dist = dist_manager.create_dist(domain, cert)
        print("Waiting for distribution deployment...")
        dist_manager.await_deploy(dist)

    zone = domain_manager.find_hosted_zone(domain) \
        or domain_manager.create_hosted_zone(domain)

    domain_manager.create_cf_domain_record('Z02674283FXKHIDDU48JQ', domain, dist['DomainName'])

    print("Domain configured: https://{}".format(domain))

    return


if __name__ == '__main__':
    cli()
