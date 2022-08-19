## References

<https://faun.pub/kubernetes-distributed-performance-testing-using-locust-871b46ba5c9c>
<https://github.com/eon01/kubernetes-locust-example>

## Requirements

Before proceeding, ensure that your environment satisfies the requirements; start by installing and deploying Docker, Kubernetes, and Git.

## Locust: Docker Images

The next step is building Docker images for Locust master and slave workers with the defined use cases. These Docker images will be used later to deploy Locust components on the cluster.

This is how the Locust Docker image file structure looks like.

Our Docker image must include at least the following files:

Dockerfile: This file will contain the needed instructions to build our Docker image.

requirements.txt: This file includes a list of Python libraries needed to run Locust.

test-case.py: This is the test case file written in Python.

run.sh: A shell script that works as an entrypoint for Docker to support master and slave workers. Below is how this file looks like:

> cd docker

> docker build -t locust:v1 .

##  Locust: Deploying in Distributed Mode

Now that we created the Docker image for our test cases, it is time to start deploying a distributed Locust cluster, and we are going to use Kubernetes for that. Note that you can deploy Locust on a single VM without Kubernetes, but in case you need a distributed testing, a Kubernetes cluster is the ideal choice to use.

To achieve this task we need to create the following Kubernetes resources.

Our Docker image must include at least the following files:

Locust master deployment.

Locust master service.

Locust worker deployment.

All the above resources are standard Kubernetes objects. The most critical factors in defining these objects are providing each of the objects with the correct values for the needed environment variables and exposing the correct ports.

Below is the definition file for the master deployment.

As shown in the definition file, it is very important to pass the environment variables LOCUST_MODE and TARGET_HOST to the container; otherwise, the containers will not be configured to run as a master Locust instance.

The Locust interface will be accessible on the following URL: <http://localhost:30627>

> cd locust/k8s

> kubectl apply -f .
