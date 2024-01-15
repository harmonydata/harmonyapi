sed s#http://localhost:8000#https://api.harmonydata.ac.uk#g test_parse_local.py  > test_parse_remote.py
sed s#http://localhost:8000#https://api.harmonydata.ac.uk#g test_match_local.py  > test_match_remote.py
sed s#http://localhost:3000#https://harmonydata.ac.uk#g test_selenium_local.py  > test_selenium_remote.py