from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import urllib.parse
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

def h2oframes():
    """
    h2o.frames()

    Testing the h2o.frames() command here.

    :return: none if test passes or error message otherwise
    """
    try:
        h2o.remove_all()    # remove all objects first
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        arrestsH2O = h2o.upload_file(pyunit_utils.locate("smalldata/pca_test/USArrests.csv"))
        prostate = h2o.upload_file(pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"))
        all_frames_summary = h2o.frames()
        pyunit_utils.verify_return_type("h2o.frames()", "H2OResponse", all_frames_summary.__class__.__name__)
        assert len(all_frames_summary['frames'])==3, "h2o.frames() command is not working.  It did not fetch all 3 " \
                                                     "frame summaries."
        total_columns = training_data.ncol+arrestsH2O.ncol+prostate.ncol
        summary_total_columns = all_frames_summary['frames'][0]['columns']+all_frames_summary['frames'][1]['columns']\
                                +all_frames_summary['frames'][2]['columns']
        assert total_columns==summary_total_columns, "Wrong frame columns are returned in frame summary.  " \
                                                     "h2o.frames() command is not working."
        total_rows = training_data.nrow+arrestsH2O.nrow+prostate.nrow
        summary_total_rows = all_frames_summary['frames'][0]['rows']+all_frames_summary['frames'][1]['rows'] \
                                +all_frames_summary['frames'][2]['rows']
        assert total_rows==summary_total_rows, "Wrong frame rows are returned in frame summary.  " \
                                               "h2o.frames() command is not working."
    except Exception as e:
        assert False, "h2o.frames() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oframes)
else:
    h2oframes()
