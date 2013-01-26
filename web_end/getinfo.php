<?php
include("dbconnect.php");

$name = $_GET["name"];
$guid = $_GET["guid"];

mysql_select_db("globan", $con);

$result = mysql_query("SELECT * FROM bans WHERE name='$name' AND guid='$guid'");
if(mysql_num_rows($result)==0)
	{
	echo "None";
	}
else
{
while($row = mysql_fetch_array($result))
  {
  echo $row["servercount"];
  }
}
?>
