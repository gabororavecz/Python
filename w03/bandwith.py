#Variables
maximum_network_bandwith = 1000000000
number_of_concurrent_users = 200
application_a= 200000
application_b = 100000
application_c = 350000

#Calculations
network_capacity= 1000*1000000 #This calculates the network capacity
current_usage= application_b + application_a #This calculates the current usage
current_availability = maximum_network_bandwith - (application_a + application_b) #This calculates the current availability
new_applications_requirements = 350000
bandwith_available_after_= (maximum_network_bandwith - ((application_a + application_b +\
application_c)*number_of_concurrent_users))/1000000 #This calcuates the bandwith available if the new application is installed in Mbps

#Output
print("The network capacity: {:.2f} bps" .format(network_capacity))
print("The current usage: {:.2f}  bps" .format(current_usage))
print("The current availability: {:.2f} bps" .format(current_availability))
print("The new applications requirements: {:.2f} bps" .format(new_applications_requirements))
print("The bandwidth available if the new application is installed: {:.2f} Mbps" .format(bandwith_available_after_))