from diagrams import Diagram, Cluster
#from diagrams.aws.compute import EC2
#from diagrams.aws.database import RDS
#from diagrams.aws.network import ELB

from diagrams.gcp.compute import AppEngine, Functions
from diagrams.gcp.database import BigTable
from diagrams.gcp.analytics import PubSub, Dataflow, BigQuery
from diagrams.gcp.iot import IotCore
from diagrams.gcp.storage import GCS

#with Diagram("web server"):
#	ELB("elb") >> EC2("web") >> RDS("user db")

with Diagram("message collecting"):

    pubsub = PubSub("pubsub")

    with Cluster("Source of Data"):
        [IotCore("core1"),
         IotCore("core2"),
         IotCore("core3")] >> pubsub

    with Cluster("Targets"):
        with Cluster("Data Flow"):
            flow = Dataflow("data flow")

        with Cluster("Data Lake"):
            flow >> [BigQuery("bq"),
                     GCS("storage")]

    with Cluster("Event Driven"):
            with Cluster("Processing"):
                flow >> AppEngine("engine") >> BigTable("bigtable")

            with Cluster("Serverless"):
                flow >> Functions("func") >> AppEngine("appengine")

    pubsub >> flow
