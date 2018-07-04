Usage Guide
===========

Usage ( *XMLRPC* )
******************

+ 1. Create JSON configuration ( runtime or read from file, *read config section* )
+ 2. Instance **testlink_manager** object ``testlink_manager = TLManager(settings=my_json_config)``
+ 3. Use some *method name with prefix* '**api_**'

**api_login**
+++++++++++++

* **XMLRPC**: *call to method named* '*tl.checkDevKey*'
* **Description** : check if dev_key it's valid

**api_tprojects** 
+++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getProjects*'
* **Description** : get all test projects


**api_tproject**
++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestProjectByName*'
* **Description** : get one test project filtered by name

**api_tproject_tplans** 
+++++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getProjectTestPlans*'
* **Description** : get all test plans for one test project

**api_tproject_tsuites_first_level**
++++++++++++++++++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getFirstLevelTestSuitesForTestProject*'
* **Description** : get all test suites on first level for one test project

**api_tplan**
+++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestPlanByName*'
* **Description** : get one test plan filtered by project and plan names

**api_tplan_platforms**
+++++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestPlanPlatforms*'
* **Description** : get one test plan filtered by project and plan names

**api_tplan_builds**
++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getBuildsForTestPlan*'
* **Description** : get all builds for test project filtered by id

**api_tplan_tsuites**
+++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestSuitesForTestPlan*'
* **Description** : get all test suites assigned to test plan filtered by id

**api_tplan_tcases**
++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestCasesForTestPlan*'
* **Description** : get all test cases assigned to test plan filtered by id

**api_tplan_build_latest**
++++++++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getLatestBuildForTestPlan*'
* **Description** : get latest build by choosing the maximum build id for a specific test plan id

**api_tplan_totals**
++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTotalsForTestPlan*'
* **Description** : get totals for testplan filtered by id

**api_tsuite**
++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestSuiteByID*'
* **Description** : get test suite filtered by id

**api_tsuite_tsuites**
++++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestSuitesForTestSuite*'
* **Description** : get test suites down of tree for one test suite filtered by id

**api_tcase**
+++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestCase*'
* **Description** : get test case filtered by id or external id

**api_tcase_by_name**
+++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.getTestCaseIDByName*'
* **Description** : get test case filtered by name

**api_tcase_report**
++++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.reportTCResult*'
* **Description** : reports a result for a single test case

**api_user_exist**
++++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.doesUserExist*'
* **Description** : check if user name it's valid

**api_about**
+++++++++++++

* **XMLRPC**: *call to method named* '*tl.about*'
* **Description** : get default message with author and testlink version

**api_say_hello**
+++++++++++++++++

* **XMLRPC**: *call to method named* '*tl.sayHello*'
* **Description** : get **'Hello!'** message

**api_ping**
++++++++++++

* **XMLRPC**: *call to method named* '*tl.ping*'
* **Description** : get **'Hello!'** message

**api_ping**
++++++++++++

* **XMLRPC**: *call to method named* '*tl.repeat*'
* **Description** : get **You said: 'your message here'** as message
