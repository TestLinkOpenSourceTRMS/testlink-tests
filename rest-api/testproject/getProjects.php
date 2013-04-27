<?php
/**
 * @filesource getProjects.php
 * Bare bones test for REST API GET /testprojects
 * 
 * @author Francisco Mancardi (francisco.mancardi@gmail.com)
 *
 */
require '../lib/pest/Pest.php';

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
  $pest = new Pest('http://localhost/development/tlrepo/lib/api/rest/v1/');
}

$password = $user = 'dev01';
$pest->setupAuth($user, $password);

echo '<b>Access ALL TESTPROJECTS</b><br>';
$thing = json_decode($pest->get('/testprojects'));
echo '<pre>';var_dump($thing);echo '<pre><br>';


echo '<b>Access Only ONE TESTPROJECT</b><br>';
$ox = (object) array('id' => 1208);
echo 'Route:' . '/testprojects/' . $ox->id;
  
$thing = json_decode($pest->get('/testprojects/' . $ox->id));
echo '<pre>';var_dump($thing);echo '<pre><br>';



echo '<b>Access Only ONE TESTPROJECT</b><br>';
$ox = (object) array('id' => 'Slim REST Framework');
echo 'Route:' . '/testprojects/' . $ox->id;
  
$thing = json_decode($pest->get('/testprojects/' . urlencode($ox->id)));
echo '<pre>';var_dump($thing);echo '<pre><br>';
