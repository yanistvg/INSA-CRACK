<?php
session_start();
session_destroy(); /* détruire la session */
session_unset();
setcookie('PHPSESSID', ", time()-3600,'/', ", 0, 0);
header("location:index.php");



?>