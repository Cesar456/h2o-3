from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import random

# DISCLAMINER
#
# The main function of API tests is to make sure that changes to the API are captured
# before the customers do.  This is to prevent breaking the customer code.  If the
# changes are necessary, we will have the chance to warn them about the changes.
#
# All API tests should be short and fast to run.  The main purposes of API tests are to
# make sure that the command in its most popular forms run correctly when user types in
# correct input arguments.  Light weight checking will be provided on the command output
# to make sure that we are getting the correct responses.
#
# For exhaustive tests using all possible combination of input arguments, making sure all
# responses of the API commands are correct, or if in error, the correct error messages
# are sent should be done elsewhere.

def h2oset_timezone():
    """
    h2o.set_timezone(value)
    Deprecated, set h2o.cluster().timezone instead.

    Testing the h2o.set_timezone() command here.  Copy from pyunit_get_set_list_timezones.py

    :return: none if test passes or error message otherwise
    """
    try:
        origTZ = h2o.get_timezone()
        print("Original timezone: {0}".format(origTZ))

        timezones = h2o.list_timezones()
        # don't use the first one..it's a header for the table
        print("timezones[0]:", timezones[0])
        zone = timezones[random.randint(1,timezones.nrow-1),0].split(" ")[1].split(",")[0]
        print("Setting the timezone: {0}".format(zone))
        h2o.set_timezone(zone)

        newTZ = h2o.get_timezone()
        assert newTZ == zone, "Expected new timezone to be {0}, but got {01}".format(zone, newTZ)

        print("Setting the timezone back to original: {0}".format(origTZ))
        h2o.set_timezone(origTZ)
    except Exception as e:
        assert False, "h2o.set_timezone() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oset_timezone)
else:
    h2oset_timezone()
