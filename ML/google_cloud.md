** This file contains some of the notes taken during the Cloud Developer Learning Path.

- Load Balancer and VPC - Load Balancer can be both on Layer 7 (Application) and distribute traffic on HTTP/HTTPS; and on Layer 4 (Networking Layer) if the application requires load balancing on other ports or protocols (e.g., UDP)
- By default, any project comes with several firewall rules and routing tables predefined. It is impossible to even create a VM without the VPC defined (either default or custom-made). In case the default VPC is deleted, it is easy to create a new one with the 
same default items, just select the "auto-populate"
- Project Name is the only thing that can be changed. The project ID is unique and assigned
- Basic Roles and Predefined Roles: Basic roles are quite broad, and it is better to use the predefined ones or create custom ones if needed
- Assign permissions to groups and not individual users
- Storage options include both SQL and NoSQL solutions. Cloud Storage is used to store blobs. BigQuery is a modern solution for data warehousing. It supports historical data querying
- Big Table is a solution for NoSQL storage - it supports heavy analytics but does not support SQL; Firestore is a solution for storing smaller files - it supports offline caching and updates
- In the lab, I created the VM instance, the MySQL instance, a user to access this DB, and a cloud storage

Google Cloud


Kubernetes:
GKE is an orchestration platform for containers. The smallest piece is called a "Pod". A Cluster contains one or more pods + control plane to control them. Service groups contain several Pods with stable IP addresses. The "kubectl" command is related to Kubernetes, like "kubectl scale". The deployment config file (.yaml) can be used to create infrastructure declaratively

GKE:
Google Kubernetes Service is an orchestration framework for Kubernetes.
GKE manages all the infrastructure for the pods and containers
Autopilot mode allows the automation for networking, IP addresses and such
Standard mode makes a user responsible for these.
GKE includes Load Balancing, Auto scaling, Auto Upgrades, Auto logging, Auto Repair

Cloud Run:
stateless containers that run in the cloud without infrastructure. Fast, scale up automatically. Wrote Code -> Build and Package -> Deploy -> get unique https URL back 
Any language can be used to build these functions
The only thing we need is to handle web requests.
Billed in 100 ms.
Cloud Run functions are even smaller - it's the serverless/functions

Best Practices for the Cloud:
Try breaking and refactoring the monolithic apps into microservices for maintainability.
Use caching like Memorystore (Redis) for frequently used data
Apigee is a platform for APIs. Use it to connect backend (including the legacy apps) with the APIs.
Use federated identity management ("Sign in with Google") - Identity Platform/Firebase auth.
Use logging with Google Cloud observability.
Implement CI/CD to avoid large deployments: Code Repo -> Cloud Build -> Artifact registry -> Cloud Deploy -> Cloud Run / GKE.
Cloud APIs:
Use these to make calls to and from the apps (HTTP, JSON, gRPC)

Cloud Shell and SDK:
Cloud Shell is available as an add-on for many IDEs
Cloud Shell provides a temporary, simple VM The Google Cloud SDK comes pre-installed and with permissions to use your cloud resources.
Cloud Code is an integration into popular IDEs, integrates with Secret Manager. It also allows working with GKE within IDE

STORAGE:
Cloud Storage - 5tb- files for unstructured data
Firestore - NoSQL database that scales, for mobile and web apps
BigTable - NoSQL database to store sparsely populated data, for big data and analytics, ideal for MapReduce
Cloud SQL - RDBMS, structured data, just like a typical DB
AlloyDB - PostgreSQL for high-performance applications, it is faster than standard PostgreSQL
Spanner - fully-managed SQL database, designed for OLTP, high availability, and global and multi-region replication, with very high uptime
BigQuery - used for ML, GIS, and BI. Fast, designed for analytics (OLAP), has Memorystore that works with Redis and Memcached
use these to make calls to and from the apps (HTTP, JSON, gRPC)

Cloud Shell and SDK:
Cloud Shell is available as an add-on for many IDEs

Authentication and Authorization
Google Cloud AIM is serving the auth. purposes.
IAM Authorization allows granular control over access to the resources.
Roles are where we assign the permissions to the resources.
There are three types of roles: Basic (not recommended - too broad), Predefined - granular access, and Custom - used when predefined are too broad.
Authentication proves who you are: API keys (rarely used), OAuth keys, and Service accounts (preferred)

