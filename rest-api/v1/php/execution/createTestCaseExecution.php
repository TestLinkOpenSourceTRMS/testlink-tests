<?php
/**
 * @filesource createTestProject.php
 * Bare bones test for REST API PUT /testprojects
 * 
 * @author Francisco Mancardi (francisco.mancardi@gmail.com)
 * @internal revisions
 *
 * 20130427
 * I've done first test using Pest.php, but when trying to use Slim request->getBody()
 * I've got always null.
 * Seems that POST BODY is not created.
 *
 * Changing to PestJSON.php, did the trick
 *
 */

require '../../../common/pest/PestJSON.php';

if(!isset($_REQUEST['env']))
{
  die('env not provided: valid options: bit,gito - call URL?env=');
}  

if($_REQUEST['env'] == 'bit')
{
  $pest = new PestJSON('http://localhost/development/bitbucket/testlink/lib/api/rest/v1/');
} 

if($_REQUEST['env'] == 'gito')
{
  $pest = new PestJSON('http://localhost/development/tlrepo/lib/api/rest/v1/');
}

$password = $user = 'dev01';
$pest->setupAuth($user, $password);

$item = array();
$item['testPlanID'] = 1185;
$item['buildID'] = 1;
$item['platformID'] = 0;
$item['testCaseExternalID'] = 'TX::1';
$item['notes'] = 'This is an execution created via REST API';
$item['statusCode'] = 'p';
$item['executionType'] = 1;
$item['executionTimeStamp'] = '2012-03-27 06:09:00';




// How to test using cUrl
// curl -i -X POST --data "jsonFile"-u dev01:dev01 http://localhost/development/tlrepo/lib/api/rest/v1/testprojects
// -i include headers
// -X (HTTP) Specifies a custom request method to use when communicating with the HTTP server  

echo '<br>IN CLIENT<br>';
$xx = json_encode($item);
var_dump($xx);

echo '<br><br><b>THING GOT FROM SERVER</b><br>';
$thing = $pest->post('/executions',$item);
var_dump($thing);
