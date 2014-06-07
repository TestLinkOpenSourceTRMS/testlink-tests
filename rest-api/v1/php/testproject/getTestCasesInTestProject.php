<?php
/**
 * @filesource getTestPlansInTestProjects.php
 * Bare bones test for REST API GET /testprojects
 * 
 * @author Francisco Mancardi (francisco.mancardi@gmail.com)
 *
 */
require '../../../common/pest/Pest.php';

if(!isset($_REQUEST['env']))
{
  die('env not provided: valid options: bit,gito - call URL?env=');
}  

if($_REQUEST['env'] == 'bit')
{
  $pest = new Pest('http://localhost/development/bitbucket/testlink/lib/api/rest/v1/');
} 

if($_REQUEST['env'] == 'gito')
{
  // How to test using cUrl
  // curl -i -X GET 
  // -i include headers
  // -X (HTTP) Specifies a custom request method to use when communicating with the HTTP server  
  $pest = new Pest('http://localhost/development/test_tl/testlink/lib/api/rest/v1/');
}

$password = $user = 'admin';
$pest->setupAuth($user, $password);

echo '<b>Access ALL TEST CASES present in a test project </b><br>';
$thing = json_decode($pest->get('/testprojects/94/testcases'));
echo '<pre>';var_dump($thing);echo '<pre><br>';
