REM --------to run a test in chromium browser--------------------------------

REM pytest -s -v --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser chromium

pytest -s -v -m "sanity"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser chromium

REM pytest -s -v -m "regression"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser chromium

REM pytest -s -v -m "sanity and regression"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser chromium

REM pytest -s -v -m "sanity or regression"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser chromium

REM --------to run a test in firefox browser--------------------------------

REM pytest -s -v --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser firefox

REM pytest -s -v -m "sanity"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser firefox

REM pytest -s -v -m "regression"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser firefox

REM pytest -s -v -m "sanity and regression"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser firefox

REM pytest -s -v -m "sanity or regression"  --html=Saucedemo_new_E2E_test/reports/reports.html Saucedemo_new_E2E_test\test_cases\all_test_combined.py --browser firefox


