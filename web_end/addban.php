<?php
include("dbconnect.php");

$name = $_POST["name"];
$guid = $_POST["guid"];


mysql_select_db("globan", $con);

$name = mysql_real_escape_string($name);
$guid = mysql_real_escape_string($guid);

$result = mysql_query("SELECT * FROM bans WHERE name='$name' AND guid='$guid'");
if(mysql_num_rows($result)==0)
	{
	echo "none found!\n";
	mysql_query("INSERT INTO bans (`name`, `guid`) VALUES ('$name', '$guid')");
	}
else
	{
	echo "exsist!\n";
	mysql_query("UPDATE bans SET servercount = servercount+1 WHERE name='$name' AND guid='$guid'");
	}
	
echo "OK";

?>