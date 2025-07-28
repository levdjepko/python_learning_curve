* This file contains some of the notes taken during the Cloud Developer Learning Path.

- Load Balancer and VPC - Load Balancer can be both on Layer 7 (Application) and distribute traffic on HTTP/HTTPS; and on Layer 4 (Networking Layer) if the application requires load balancing on other ports or protocols (e.g., UDP)
- By default, any project comes with several firewall rules and routing tables predefined. It is impossible to even create a VM without the VPC defined (either default or custom-made). In case the default VPC is deleted, it is easy to create a new one with the 
same default items, just select the "auto-populate"
- Project Name is the only thing that can be changed. The project ID is unique and assigned
- Basic Roles and Predefined Roles: Basic roles are quite broad, and it is better to use the predefined ones or create custom ones if needed
- Assign permissions to groups and not individual users
- Storage options include both SQL and NoSQL solutions. Cloud Storage is used to store blobs
