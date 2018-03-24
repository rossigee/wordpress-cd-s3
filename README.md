# AWS S3 deployment driver

Deploys plugins, themes and site builds to S3 buckets.

Requires the '[wordpress-cd](https://github.com/rossigee/wordpress-cd)' package.

Requires the following environment variables to be made available:

Env var | Description | Example
--------|-------------|--------
WPCD_S3_PREFIX | The bucket and path to upload the ZIP file to | s3://my-artifacts-bucket/wordpress/plugins

It invokes the 'aws' CLI in a subprocess, so will require either a valid AWS configuration file available, or the relevant 'AWS_*' environment variables set.
