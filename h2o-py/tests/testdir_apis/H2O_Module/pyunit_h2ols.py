from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

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

def h2ols():
    """
    h2o.ls()

    Testing the h2o.ls() command here.

    :return: none if test passes
    """
    try:
        iris = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris.csv"))
        lsObject = h2o.ls()
        # check return type as DataFrame
        pyunit_utils.verify_return_type("h2o.ls()", "DataFrame", type(lsObject).__name__)
        # check that our frame info was included in the lsObject
        assert lsObject.values[0][0] == str(iris.frame_id), \
            "Frame info iris.hex should have been found but h2o.ls() command failed."
    except Exception as e:
        assert False, "h2o.ls() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ols)
else:
    h2ols()
