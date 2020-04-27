
Download all jobs
------------------

    python dl-jenkins.py

Restore a job
----------------

* Disable CRUMB /CRSF in jenkins, see https://stackoverflow.com/a/57869141
* See [documentation](https://support.cloudbees.com/hc/en-us/articles/218353308-How-to-update-job-config-files-using-the-REST-API-and-cURL-)

    JOB_TO_RESTORE=juliac
    curl -X POST -u martin.monperrus@inria.fr "https://ci.inria.fr/sos/job/$JOB_TO_RESTORE/config.xml" --data-binary "@jobs/$JOB_TO_RESTORE.xml"
