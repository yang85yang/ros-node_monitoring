#! /usr/bin/env python

#---------------------------------------------------------------------------
#  publisher.py - Node monitoring state publisher test
#
#  Created: Thu Apr 14 01:01:58 2011
#  Copyright  2011  Tim Niemueller [www.niemueller.de]
#             2011  SRI International
#             2011  Carnegie Mellon University
#             2011  Intel Labs Pittsburgh
#             2011  Columbia University in the City of New York
#
#---------------------------------------------------------------------------


#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the 3-clase BSD License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Library General Public License for more details.
#
#  Read the full text in the LICENSE file in the root directory.
#

import roslib; roslib.load_manifest('nodemon_py')
import rospy

from nodemon.state_publisher import NodeStatePublisher

if __name__ == '__main__':
    rospy.init_node('nodemon_example_publisher')
    node_state = NodeStatePublisher()
    node_state.set_running()
    rospy.spin()
    node_state = 0
