from __future__ import print_function
from builtins import str
from builtins import range
import sys, os
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.estimators.glm import H2OGeneralizedLinearEstimator

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

def h2odownload_pojo():
    """
    h2o.download_pojo(model, path=u'', get_jar=True)

    Testing the h2o.download_pojo() command here.  Copied from glm_download_pojo.py

    :return: none if test passes or error message otherwise
    """
    try:
        h2o_df = h2o.import_file(pyunit_utils.locate("smalldata/prostate/prostate.csv"))
        h2o_df['CAPSULE'] = h2o_df['CAPSULE'].asfactor()
        binomial_fit = H2OGeneralizedLinearEstimator(family = "binomial")
        binomial_fit.train(y = "CAPSULE", x = ["AGE", "RACE", "PSA", "GLEASON"], training_frame = h2o_df)
        try:
            results_dir = pyunit_utils.locate("results")    # find directory path to results folder
            h2o.download_pojo(binomial_fit,path=results_dir)
            assert os.path.isfile(os.path.join(results_dir, "h2o-genmodel.jar")), "h2o.download_pojo() " \
                                                                                  "command is not working."
        except:
            h2o.download_pojo(binomial_fit)     # just print pojo to screen if directory does not exists
    except Exception as e:
        assert False, "h2o.download_pojo() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2odownload_pojo)
else:
    h2odownload_pojo()
