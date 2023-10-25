from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, ECS, EKS, Lambda
from diagrams.aws.database import RDS, Redshift
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.aws.integration import SQS

with Diagram("Event Processing"):
#	ELB("elb") >> EC2("web") >> RDS("user db")

	source = EKS("k8s source")
	
	with Cluster("Event Flows"):
		with Cluster("Event workers"):
			workers = [ECS("w1"), ECS("w2"), ECS("w3")]

		queue = SQS("event queue")

		with Cluster("Processing"):
			handlers = [Lambda("proc1"), Lambda("proc2"), Lambda("proc3")]

	store = S3("events store")
	dw = Redshift("analytics")

	source >> workers >> queue >> handlers
	handlers >> store
	handlers >> dw
