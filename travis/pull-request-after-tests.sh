#!/bin/bash
# executed after having run the tests of spoon-core
# the main advantage is that one can get some information in surefire-reports

# example task
echo number of executed test classes: `ls target/surefire-reports | wc`

