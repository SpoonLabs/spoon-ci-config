
To download all jobs:

    python dl-jenkins.py

To restore a job [doc](https://support.cloudbees.com/hc/en-us/articles/218353308-How-to-update-job-config-files-using-the-REST-API-and-cURL-)

    curl -X POST http://developer:developer@localhost:8080/job/test/config.xml --data-binary "@mymodifiedlocalconfig.xml"

    curl -X POST -u martin.monperrus@inria.fr https://ci.inria.fr/sos/job/Website%20Deployer/config.xml --data-binary "@jobs/Website Deployer.xml"
