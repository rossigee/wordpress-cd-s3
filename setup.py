from setuptools import setup

setup(name = 'wordpress-cd-s3',
    version = '0.1.0',
    description = 'Rancher driver to deploy WP artifacts to S3 buckets.',
    author = 'Ross Golder',
    author_email = 'ross@golder.org',
    url = 'https://github.com/rossigee/wordpress-cd-s3',
    packages = [
      'wordpress_cd_s3',
    ]
)
