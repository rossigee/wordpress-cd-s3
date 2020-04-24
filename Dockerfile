FROM rossigee/wordpress-cd

RUN pip install awscli

# Install the CI scripts
ADD dist /dist
RUN pip install /dist/wordpress-cd-s3-0.2.2.tar.gz
