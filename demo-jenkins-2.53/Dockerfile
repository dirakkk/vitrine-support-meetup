# Use the Jenkins base image
FROM jenkins/jenkins:2.53

# Switch to root to install Node.js
USER root

# Install Node.js 23 using n or directly via NodeSource (adjust for your preferred installation method)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_23.x | bash - && \
    apt-get install -y nodejs && \
    node -v && npm -v

# Switch back to Jenkins user
USER jenkins
