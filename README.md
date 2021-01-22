# awsdrones
$ pipenv --python 3.8

# Used AWS Zone  ---- >>>> us-east-1

$ git log
$ git checkout -b dev commit-ID(By log)
$ git status

$ git checkout domain|website.domain.com|rekognition|master|dev|etc

# s3dron currently has the following features:

- List bucket
- List contents of a bucket
- Create and set up bucket
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName>

##### Set of commands working
$ python s3dron/s3dron.py --help
Usage: s3dron.py [OPTIONS] COMMAND [ARGS]...

  s3dron deploys websites to AWS.

Options:
  --profile TEXT  Use a given AWS profile.
  --help          Show this message and exit.

Commands:
  list-bucket-objects  List objects in an s3 bucket.
  list-buckets         List all s3 Buckets.
  setup-bucket         Create and configure S3 bucket.
  sync                 Sync contents of PATHNAME to Bucket.


#####################################

python s3dron/s3dron.py setup-bucket automatingdomain-boto3

python s3dron/s3dron.py --help

python s3dron/s3dron.py list-buckets

python s3dron/s3dron.py sync s3_reactjs automatingdomain-boto3

python s3dron/s3dron.py --profile=boto3dev sync s3_reactjs automatingdomain-boto3

python s3dron/s3dron.py --profile=boto3dev setup-domain test.servicediscover.local

python s3dron/s3dron.py --profile=boto3dev  find-cert test2.domain.com

############################ Prod Test ################################

python s3dron/s3dron.py --profile=boto3dev setup-bucket test2.domain.com

python s3dron/s3dron.py --profile=boto3dev list-buckets

python s3dron/s3dron.py sync s3_reactjs test.domain.com

python s3dron/s3dron.py --profile=boto3dev setup-domain test2.domain.com

python s3dron/s3dron.py --profile=boto3dev  find-cert test2.domain.com


#  Create 100 mb file to test upload sync time for old files it must skipp old files

$ dd if=/dev/zero of=test.img bs=1024 count=0 seek=$[1024*100]

# ServerLess 

$ serverless create --template aws-python3  --name alertdron-alerts
