import boto3

aws_mag_con = boto3.session.Session(profile_name='default')

service = boto3.resource(service_name='iam')


# listing IAM users with resource obj
for each in service.users.all():
    print(each.name)

