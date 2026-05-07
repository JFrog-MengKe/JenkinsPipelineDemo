#!/usr/bin/env bash
# Apply generated config.xml to a Jenkins controller (replace JOB_DIR with your job path).
# Usage:
#   python3 scripts/build_maven_jenkins_config.py | sudo tee /var/lib/jenkins/jobs/MY_JOB/config.xml >/dev/null
#   sudo chown jenkins:jenkins /var/lib/jenkins/jobs/MY_JOB/config.xml
# Or copy from config/examples after generating locally:
#   python3 scripts/build_maven_jenkins_config.py > config/examples/maven-job-generated.xml
set -euo pipefail
echo "See docs/controller-setup.md — this script is a reminder only; paths vary by installation."
