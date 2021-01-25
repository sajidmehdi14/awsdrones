# Server Less setup for AWS Lambda

sudo apt install nodejs npm

npm install -g serverless

 cd awsdron/alertdrone/

 mkdir alerts

 cd alerts/

 serverless create --template aws-python3 --name alertdrone-alerts

 atom .

 cp serverless.yml serverless.yml-org

 cat serverless.yml

 cat handler.py 

 sls deploy

 echo $?
