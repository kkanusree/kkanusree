// feedback.php
<?php
$con = mysql_connect("localhost","root","");
if (!$con)
	{
	die('could not connect: ' .  mysql_error());
	}
mysql_select_db("demo", $con);
$sql="INSERT INTO feedback VALUES
('$_POST[name]', '$_POST[contact]',
'$_POST[email id]', '$_POST[comment]')";
if (!mysql_query($sql,$con))
{
die('Error in posting values: ' .  mysql_error());
}
echo "feedback is stored in the table successfully";
mysql_close($con)
?>