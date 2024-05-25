sed s#http://localhost:8000#https://api.harmonydata.ac.uk#g local_tests/test_parse_local.py  > remote_tests/test_parse_remote.py
sed s#http://localhost:8000#https://api.harmonydata.ac.uk#g local_tests/test_match_local.py  > remote_tests/test_match_remote.py
sed s#http://localhost:8000#https://api.harmonydata.ac.uk#g local_tests/test_match_mhc_local.py  > remote_tests/test_match_mhc_remote.py
sed s#http://localhost:8000#https://api.harmonydata.ac.uk#g local_tests/test_different_frameworks_local.py  > remote_tests/test_different_frameworks_remote.py
sed s#http://localhost:3000#https://harmonydata.ac.uk#g selenium_tests/test_selenium_local.py  > selenium_tests/test_selenium_remote.py