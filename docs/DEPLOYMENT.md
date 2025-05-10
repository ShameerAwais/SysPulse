# SysPulse Deployment Guide

This guide will help you deploy SysPulse on your own AWS infrastructure.

## Prerequisites

1. **AWS Account Setup**
   - An AWS account with appropriate permissions
   - AWS CLI installed and configured
   - AWS access key and secret key

2. **Required Tools**
   - Git
   - Docker and Docker Compose
   - Terraform (for AWS infrastructure)
   - Python 3.8+

## Deployment Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/SysPulse.git
cd SysPulse
```

### 2. AWS Setup

1. **Create an AWS Key Pair**
   - Go to AWS Console → EC2 → Key Pairs
   - Click "Create Key Pair"
   - Name it (e.g., "syspulse-key")
   - Download the .pem file
   - Keep it secure (you'll need it for SSH access)

2. **Configure AWS Credentials**
   ```bash
   aws configure
   # Enter your AWS Access Key ID
   # Enter your AWS Secret Access Key
   # Enter your preferred region (e.g., us-east-1)
   ```

### 3. Terraform Configuration

1. **Update Variables**
   Edit `Terraform/variables.tf` or create `terraform.tfvars`:
   ```hcl
   aws_region = "your-region"  # e.g., us-east-1
   ami_id     = "your-ami-id"  # Ubuntu 22.04 LTS AMI ID for your region
   key_name   = "your-key-name"  # The key pair you created
   ```

2. **Initialize Terraform**
   ```bash
   cd Terraform
   terraform init
   ```

3. **Deploy Infrastructure**
   ```bash
   terraform apply
   ```

### 4. Application Deployment

1. **Build and Push Docker Image**
   ```bash
   docker build -t syspulse-app .
   docker tag syspulse-app your-dockerhub-username/syspulse-app:latest
   docker push your-dockerhub-username/syspulse-app:latest
   ```

2. **SSH into EC2 Instance**
   ```bash
   ssh -i path/to/your-key.pem ubuntu@your-ec2-public-ip
   ```

3. **Run Application**
   ```bash
   # On EC2 instance
   docker pull your-dockerhub-username/syspulse-app:latest
   docker run -d -p 8000:8000 your-dockerhub-username/syspulse-app:latest
   ```

### 5. Access the Application

- Web Interface: `http://your-ec2-public-ip:8000`
- API Documentation: `http://your-ec2-public-ip:8000/docs`
- Prometheus: `http://your-ec2-public-ip:9090`
- Grafana: `http://your-ec2-public-ip:3000`

## Security Considerations

1. **Update Security Groups**
   - Review and modify security group rules in `Terraform/main.tf`
   - Restrict SSH access to your IP
   - Configure appropriate port access

2. **IAM Roles**
   - Use IAM roles instead of access keys when possible
   - Follow the principle of least privilege

3. **Key Management**
   - Keep your AWS key pair secure
   - Don't commit sensitive credentials to the repository

## Troubleshooting

1. **EC2 Instance Issues**
   - Check instance status in AWS Console
   - Review instance logs
   - Verify security group rules

2. **Application Issues**
   - Check Docker logs: `docker logs container_id`
   - Verify port mappings
   - Check application logs

3. **Network Issues**
   - Verify VPC and subnet configuration
   - Check route tables
   - Test network connectivity

## Maintenance

1. **Updates**
   - Pull latest changes: `git pull`
   - Rebuild Docker image
   - Restart containers

2. **Backup**
   - Regularly backup your data
   - Keep track of infrastructure changes

3. **Monitoring**
   - Set up CloudWatch alarms
   - Monitor resource usage
   - Review logs regularly

## Support

If you encounter any issues:
1. Check the [Issues](https://github.com/yourusername/SysPulse/issues) page
2. Create a new issue with detailed information
3. Include relevant logs and error messages 