#Try it yourself 9-12:Multiple Modules

from user_module import User
from privileges_admin_module import Privileges, Admin


lendog = Admin('leonard', 'beaucheman', 'aviation engineer', 'june', 1954)
lendog.privileges.show_privileges()
