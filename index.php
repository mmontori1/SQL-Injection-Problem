<!DOCTYPE html>
	<html>
		<body>
			<!-- <p>Wanna go back to the index page: <a href="/"> return? </a></p> -->
			<p>Wanna drop?: <a href="/dropdown.html"> return? </a></p>
			<!-- <a href="/"> return? </a><br> -->

			<?php
				echo "secrets are not here";
				$secrets = array("what", "is", "pass");
				echo "<br>";
				// foreach ($secrets as $value) {
				//     echo "$value";
				// }
			?>

			<form action="stuff.php" method="post">
				Name: <input type="text" name="name">
				<input type="submit">
			</form>
			<?php
   
			   $dbhost = 'localhost';
			   $dbuser = 'guest';
			   $dbpass = 'Elti90q8nB?h';
			   $conn = mysql_connect($dbhost, $dbuser, $dbpass);
			   
			   if(! $conn ) {
			      die('Could not connect: ' . mysql_error());
			   }
			   
			   echo 'Connected successfully';
			   mysql_close($conn);
			?>

		</body>
	</html>