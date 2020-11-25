To build a full CICD pipeline, using Docker, Flask, circleci, AWS-ECS

1) Enter ./circleci/config.yml

1.a) Replace NAME_OF_ECS_CLUSTER (everywhere in the file) to be the name of the ECS cluster that will be running in AWS

1.b) Replace REPO_NAME to be the name of the git repo, in github

1.c) Replace NAME_OF_ECS_SERVICE to be the name of the ECS "service" that will run on the EVS cluster.

1.d) ensure that your AWS region is set to that of the CLUSTER
-e AWS_DEFAULT_REGION=eu-central-1   

2) Modify your Dockerfile, so that it builds sucessfully.

3) Add all of your unit tests to the test/ directory

  -- all tests should start with test_... e.g. test_filename1.py

  -- all functions within the test files should start def test_...():

  Ensure that your test run, by running from the command line:
  
  %>pip install -r requirements.txt
  
  and
  
  %>pytest



*** this is where things get a bit difficult! ***
https://eu-central-1.console.aws.amazon.com/ecs/home?region=eu-central-1#/clusters

4) In AWS ECS set up an ECS cluster with name NAME_OF_ECS_CLUSTER (as above), in the correct AWS region.

5) Set up a Service

6) Set up a task with the properties 

6.a)

Task Definition Name: CallitSomethingMeaningful

Task Role: SecretECSTaskRole

Set: Task execution == roleSecretECSTaskRole

CompatibilitiesEC2



6.b) Container Definitions -> Add Container  &&See TaskExample.png for help

In the "Container Definitions": set a new image, and point it to  

set Image*  to be:  adludiodev/REPO_NAME:ExISTINgTagNumber

set Secrets Manager ARN: --get this from your IAM credentials??

add Port mappings if required. 

complete the creation of the task.

7) In your created cluster, e.g. 

https://eu-central-1.console.aws.amazon.com/ecs/home?region=eu-central-1#/clusters/rec-engine-cluster1/services

Select Services->Create

7.a) add a service, with the NAME_OF_ECS_SERVICE as in step 1)

7.b) Assign the task you created in 6) to it. &&See ServiceExample.png for tipps.

7.c) Ensure the following values are set.

Number of tasks 1

Minimum healthy percent 0

Maximum percent 200


8) In your created cluster,  

8.a) Assign an EC2 instance to your cluster, if not set, create one, assign ssh-keys at startup.


9)ssh onto your machine. Docker will already be running, and you can watch it, and see the version number being updated as you make more .git pushes to the master branch.

10) check out https://app.circleci.com/pipelines/github/FutureAdLabs/REPO_NAME

11) You might need to have Jonathon enable your REPO project.

12) .git push your code to master. and sit back with a beer and watch it all happen.

