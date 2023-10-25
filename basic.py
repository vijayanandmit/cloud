from diagrams import Diagram, Cluster
#from diagrams.aws.compute import EC2
#from diagrams.aws.database import RDS
#from diagrams.aws.network import ELB

from diagrams.gcp.compute import AppEngine, Functions
from diagrams.gcp.database import BigTable
from diagrams.gcp.analytics import PubSub, Dataflow
from diagrams.gcp.iot import IotCore


#with Diagram("web server"):
#	ELB("elb") >> EC2("web") >> RDS("user db")

with Diagram("message collecting"):
	pubsub = PubSub("p/s")

	with Cluster("Data Source"):
		[IotCore("core1")] >> pubsub
	
	flow = Dataflow("data flow")


	pubsub >> flow
