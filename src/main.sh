#!/bin/env sh

cd "/d/ProgramFiles/GoogleDrive/PythonCode/Project/forex_rate_scarp/src"
echo `date` "starting forex rate scarper script."
echo
/d/ProgramFiles/Python/Python37/python '/d/ProgramFiles/GoogleDrive/PythonCode/Project/forex_rate_scarp/src/main.py'
echo
echo `date` "script completed"
echo "press enter to exit."
read junk

exit 0
#eof
