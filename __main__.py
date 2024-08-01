"""A Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import pulumi_aws.ec2 as ec2
import os


#VPC Create
vpc = aws.ec2.Vpc("my-vpc",
    cidr_block = "10.10.0.0/16",
    enable_dns_hostnames = True,
    enable_dns_support = True
    )

#Inteernet Getway
igw = ec2.InternetGateway('internet-getway',
    vpc_id = vpc.id
    )

#Create subnet
#Public Subnet
pubic_subnet = ec2.subnet('public-subnet',
    vpc_id = vpc.id,
    cidr_block = "10.10.1.0/24",
    map_public_ip_on_launch = True,
    availability_zone = 'ap-southeast-1a'
)
#Privet Subnet
privet_subnet = ec2.subnet('privet-subnet',
    vpc_id = vpc.id,
    cidr_block = "10.10.2.0/24",
    map_public_ip_on_launch = False,
    availability_zone = 'ap-southeast-1a'
)

