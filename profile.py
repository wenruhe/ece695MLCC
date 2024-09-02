import geni.portal as portal
import geni.rspec.pg as rspec

# Create the first XenVM
node1 = request.XenVM("node1")
node1.disk_image = "urn:publicid:IDN+utah.cloudlab.us+image+ece69500mlcc-PG0:wenruhe"
node1.routable_control_ip = "true"

node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y apache2"))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status apache2'))

# Create the second XenVM
node2 = request.XenVM("node2")
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node2.routable_control_ip = "true"

node2.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node2.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y apache2"))
node2.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status apache2'))

# Optionally, you can define a link between nodes
link = request.Link()
link.addInterface(node1.addInterface())
link.addInterface(node2.addInterface())

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
