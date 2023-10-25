from diagrams import Diagram
from diagrams.k8s.compute  import Deployment, Pod, ReplicaSet
from diagrams.k8s.clusterconfig import HorizontalPodAutoscaler
from diagrams.k8s.network import Ingress, Service

with Diagram("exposed pod with 3 replicas"):
	net = Ingress("domain.com") >> Service("svc")

	pod = [Pod("pod1"), Pod("pod2"), Pod('pod3')]

	net >> pod << ReplicaSet('rs') << Deployment('dp') << HorizontalPodAutoscaler('hpa')