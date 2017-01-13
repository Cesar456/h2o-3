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
# make sure that the command in its most popular forms, run correctly when user types in
# correct input arguments.  Light weight checking will be provided on the command output
# to make sure that we are getting the correct responses.
#
# For exhaustive tests using all possible combination of input arguments, making sure all
# responses of the API commands are correct, or if in error, the correct error messages
# are sent should be done elsewhere.

def h2ointeraction():
    """
    h2o.interaction(data, factors, pairwise, max_factors, min_occurrence, destination_frame=None)

    Testing the h2o.interaction() command here.  Copied from pyunit_interaction.py
    :return: none if test passes or error message otherwise
    """

    try:
        iris = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris.csv"))

        # add a couple of factor columns to iris
        iris = iris.cbind(iris[4] == "Iris-setosa")
        iris[5] = iris[5].asfactor()
        iris.set_name(5,"C6")

        iris = iris.cbind(iris[4] == "Iris-virginica")
        iris[6] = iris[6].asfactor()
        iris.set_name(6, name="C7")

        # create a frame of the two-way interactions
        two_way_interactions = h2o.interaction(iris, factors=[4,5,6], pairwise=True, max_factors=10000,
                                               min_occurrence=1)
        pyunit_utils.verify_return_type("h2o.interaction()", "H2OFrame", two_way_interactions.__class__.__name__)
        assert two_way_interactions.nrow == 150 and two_way_interactions.ncol == 3, \
            "Expected 150 rows and 3 columns, but got {0} rows and {1} " \
            "columns".format(two_way_interactions.nrow, two_way_interactions.ncol)
        levels1 = two_way_interactions.levels()[0]
        levels2 = two_way_interactions.levels()[1]
        levels3 = two_way_interactions.levels()[2]

        assert levels1 == ["Iris-setosa_1", "Iris-versicolor_0", "Iris-virginica_0"], \
            "Expected the following levels {0}, but got {1}".format(["Iris-setosa_1", "Iris-versicolor_0", "Iris-virginica_0"],
                                                                    levels1)
        assert levels2 == ["Iris-setosa_0", "Iris-versicolor_0", "Iris-virginica_1"], \
            "Expected the following levels {0}, but got {1}".format(["Iris-setosa_0", "Iris-versicolor_0", "Iris-virginica_1"],
                                                                    levels2)
        assert levels3 == ["0_0", "1_0", "0_1"], "Expected the following levels {0}, but got {1}".format(["0_0", "1_0", "0_1"],
                                                                                                         levels3)
    except:
        assert False, "h2o.interaction() command not is working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ointeraction)
else:
    h2ointeraction()
