from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Grouped Workers"):
	ELB("elb") >> [EC2("w1"),
			EC2("w2"),
			EC2("w3")] >> RDS("events")
