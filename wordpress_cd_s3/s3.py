# Amazon S3-based deployment functions

import os
import subprocess
import logging
_logging = logging.getLogger(__name__)

from wordpress_cd.drivers import driver
from wordpress_cd.drivers.base import BaseDriver


@driver('s3')
class S3BucketDriver(BaseDriver):
    def __str__(self):
        return "S3"

    def __init__(self, args):
        _logging.debug("Initialising S3 Bucket Deployment Driver")
        super(S3BucketDriver, self).__init__(args)

        self.s3_prefix = os.environ['WPCD_S3_PREFIX']

    def _deploy_module(self, type):
        module_id = self.get_module_name()
        zip_file = "build/{0}.zip".format(module_id)
        s3location = "{0}/{1}.zip".format(self.s3_prefix, module_id)
        _logging.info("Deploying '{1}' {0} branch '{2}' to AWS S3 location '{3}' (job id: {4})...".format(type, module_id, self.git_branch, s3location, self.job_id))

        uploadargs = ['aws', 's3', '--acl=public-read', 'cp', zip_file, s3location]
        uploadenv = os.environ.copy()
        uploadproc = subprocess.Popen(uploadargs, stderr=subprocess.PIPE, env=uploadenv)
        uploadproc.wait()
        exitcode = uploadproc.returncode
        errmsg = uploadproc.stderr.read()
        if exitcode != 0:
            raise Exception("Error while uploading: %s" % errmsg)

        # Done
        _logging.info("Deployment successful.")
        return 0
