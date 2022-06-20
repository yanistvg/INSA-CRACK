<?php
session_start();
?>
<html>
<head>
	<title></title>
 <meta charset="utf-8">
<link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
  <nav>
  <ul>
    <li><a href="index.php">Login</a></li>
    <li><a href="inscription.php">Inscription</a></li>
      <?php
    if(isset($_SESSION['nom']))
    {
      echo '<li><a href="logout.php">Déconnexion</a></li>';
    }
    ?>
  </ul>
  </nav>
</header>
<section>
 <h1 class="titre">Page inscription</h1> 
</section>
<form action="" method="post" id="inscription" enctype="multipart/form-data">
<input type="text" name="nom" placeholder="nom" class="ch" required="required"><br>
<input type="text" name="prenom" placeholder="prenom" class="ch" required="required"><br>
<input type="email" name="email" placeholder="email" class="ch" required="required"><br>
<input type="password" name="mp1" placeholder="mot de passe" class="ch" required="required"><br>
<input type="password" name="mp2" placeholder="confirmer mot de passe" class="ch" required="required"><br>
<input type="file" name="photo" class="ch">
<input type="submit" name="valider" value="Valider" class="ch">
<?php
include("connexion.php");

if(isset($_POST['valider']))
{
	$nom=$_POST['nom'];
  $prenom=$_POST['prenom'];
  $email=$_POST['email'];
  $mp1=$_POST['mp1'];
  $mp2=$_POST['mp2'];

if($mp1==$mp2)
{
  $mp=sha1($mp1);
  $res=mysqli_query($cn,"insert into utilisateur values (NULL,'$nom','$prenom','$email','$mp')");  

$id=mysqli_insert_id($cn);
$photo="$id.jpg";

move_uploaded_file($_FILES['photo']['tmp_name'], "images/$photo");
echo 'Inscription réussie !!!';
}
else
  echo 'les mots de passe ne sont pas identiques ';

}
?>



</form>
</div>
</body>

</html>