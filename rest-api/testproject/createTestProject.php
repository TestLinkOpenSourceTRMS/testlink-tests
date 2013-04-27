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

require '../lib/pest/PestJSON.php';

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
$item['name'] = 'FrenchToJD(month, day, year)';
$item['notes'] = 'This is a FrenchToJD';
$item['color'] = '';
$item['prefix'] = 'FTJD';
$item['active'] = 1;
$item['is_public'] = 1;
$item['options'] = array();
$item['options']['requirementsEnabled']=0;
$item['options']['testPriorityEnabled'] = 1;
$item['options']['automationEnabled'] = 1;
$item['options']['inventoryEnabled'] = 0;

echo '<br>IN CLIENT<br>';
$xx = json_encode($item);
var_dump($xx);

echo '<br><br><b>THING GOT FROM SERVER</b><br>';
$thing = $pest->post('/testprojects',$item);
var_dump($thing);
