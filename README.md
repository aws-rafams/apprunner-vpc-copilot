# AppRunner VPC connection with Copilot

**Rafael Mosca\*\***, Associate Solutions Architect, WWPS EMEA Central SA\*\*

The [AWS Copilot CLI](https://aws.github.io/copilot-cli/) is a tool that since its [launch in 2020](https://aws.amazon.com/blogs/containers/introducing-aws-copilot/), developers have been using to build, manage, and operate Linux and Windows containers on [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [AWS Fargate](https://aws.amazon.com/fargate/), and [AWS App Runner.](https://aws.amazon.com/apprunner/)

Not so long ago, we announced [VPC Support for AWS App Runner](https://aws.amazon.com/blogs/aws/new-for-app-runner-vpc-support/). This means web applications and APIs that you deploy using [AWS App Runner](https://aws.amazon.com/apprunner/), can now communicate with databases running in services like [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/), and other applications running [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/), [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) that are hosted in an [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/).

Although you can enable VPC access from the AWS App Runner console following the [steps described in the documentation](https://docs.aws.amazon.com/apprunner/latest/dg/network-vpc.html), during this blog we will see how it is actually possible to enable VPC access and connect to an [Amazon Aurora](https://aws.amazon.com/rds/aurora/) database in a very easy way by using the AWS Copilot CLI.
