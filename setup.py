from setuptools import setup

setup(name = 'wordpress-cd-s3',
    version = '0.2.2',
    description = 'Rancher driver to deploy WP artifacts to S3 buckets.',
    author = 'Ross Golder',
    author_email = 'ross@golder.org',
    url = 'https://github.com/rossigee/wordpress-cd-s3',
    install_requires = [
      'wordpress-cd'
    ],
    packages = [
      'wordpress_cd_s3',
    ]
)
