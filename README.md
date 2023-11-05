# basic-event-driven-gcp
Basic Event-Driven Microservice using GCP

##Deployment
For the deployment, change to the directory and use the gcloud command
```cd gcf-1-pub```
```gcloud functions deploy my-publisher-1 --entry-point getRequest --runtime python38 --trigger-http --memory 1024 --max-instances 1000 --min-instances 0```

Like the above, use the following commands for all the deployments
```
#Deploying Publishers
gcloud functions deploy my-publisher-1 --entry-point getRequest --runtime python38 --trigger-http --memory 1024 --max-instances 1000 --min-instances 0
gcloud functions deploy my-publisher-2 --entry-point getRequest --runtime python38 --trigger-http --memory 1024 --max-instances 1000 --min-instances 0

#Deploying Subscribers
gcloud functions deploy my-subscriber-1 --entry-point getMessages --runtime python38 --trigger-topic my-gcf-topic-1 --memory 1024 --max-instances 1000 --min-instances 0
gcloud functions deploy my-subscriber-2 --entry-point getMessages --runtime python38 --trigger-topic my-gcf-topic-2 --memory 1024 --max-instances 1000 --min-instances 0
```

##Topic Creation
For creating the topics in GCP, use the below command in your Google Cloud Shell SDK
```
gcloud pubsub topics create my-gcf-topic-1
gcloud pubsub topics create my-gcf-topic-2
```

Use this repository as a template for any number of deployments to be done for your use case.
