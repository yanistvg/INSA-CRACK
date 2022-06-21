# Payday 2 CTF

Pour commencer, on doit scanner le réseau pour trouver l'IP de la VM. Une fois l'IP récupéré, nous pouvons nous connecter au site. j'en profite pour ajouter l'IP au fichier hosts et donner le nom de vhost ```crime.net``` :</br>
![image](https://user-images.githubusercontent.com/73934639/174621252-3b607145-81c2-4fd7-917c-497fd42cd773.png)

À la lecture de la page, on n’a pas l'impression qu'il y ait quoi que ce soit d'intéressant. On peut commencer par lancer du fuzzing sur le site. Je vais utiliser gobuster :</br>
![image](https://user-images.githubusercontent.com/73934639/174624164-8dbcac25-2334-4ab6-8a7c-98cca9ca0c1d.png)

Le ```plan.txt``` ne contient que les étapes du braquage, rien d'intéressant. Mais le ```robots.txt``` lui contient deux liens :</br>
![image](https://user-images.githubusercontent.com/73934639/174624536-2360dcec-357a-45c5-bc13-91a63a4727e7.png)

Si on regarde le code source de la 1ere page on tombe sur un lien vers la 2e page :</br>
```html 
<!-- Let's go inside the main hall : /main_hall -->
```
</br>
Dans le hall nous n'avons rien dans le code source. Mais on nous demande de trouver le manager. Soit nous devinons que la page se nomme "./manager" soit nous utilisons un outil pour fuzzer la page.</br>

Nous avons sur la page du manager sa carte d'accès encodé en base64 dans le code source : 
```html
<!--Card : NnIzNDdfNENDMzU1XzcwXzdIM18zbDNDN3IxQzRsX3IwME0K-->
```
Une fois décodée, la carte d'accès nous donne : ```6r347_4CC355_70_7H3_3l3C7r1C4l_r00M```
On se dirige maintenant vers la page des détecteurs de métaux trouvée précédemment. On nous demande de donner les codes d'accès. On en déduit qui faut faire une requête GET :</br>
![image](https://user-images.githubusercontent.com/73934639/174629156-30a7201d-9e3e-4e12-bc0d-4b343881cc03.png)</br>

En faisant la requête suivante, on accède à l'intérieur de la pièce : ```http://crime.net/main_hall/shutdown_the_metal_detectors/?access_code=6r347_4CC355_70_7H3_3l3C7r1C4l_r00M```.
On y trouve 3 images. On les télécharge. Grâce à stegcracker, on récupère un premier fichier dans la 1ere image. Dans la deuxième, c'est dans les données exifs de l'image que l'on trouve la 2e partie du message.
Enfin, en cherchant à l'aide de la commande ```strings``` de Linux, nous trouvons la dernière chaine. Ce qui, une fois concaténé, nous donne : ```N0gzX0YxcjU3X1cwcj FEXzg0TktfME4xWV9VNTNfNTND VXIzX1A0NTVXMHJECg==
```. Une fois décodé (base64), nous avons : ```7H3_F1r57_W0r1D_84NK_0N1Y_U53_53CUr3_P455W0rD```

On se rend maintenant sur la 2e page donnée par le fichier ```robots.txt``` et on nous demande un code. On utilise donc celui trouvé juste avant :</br>
![image](https://user-images.githubusercontent.com/73934639/174631813-838df633-b4d1-41b5-b490-3789ab0cc7ed.png)</br>

Lorsque nous validons, on nous parle de ```Funds Transfer Pricing``` et de ```Small and Medium Business```. Ce qui nous fait penser au serveur FTP et SMB.
Pour se connecter au serveur FTP, nous avons besoin de cracker un hash à l'aide d'outil en ligne. Avec [md5hashing](https://md5hashing.net/) on trouve le mot de passe : ```the_first_world_bank_is_full_with_cash```</br>
Une fois connecté au serveur FTP on trouve une note. Mais si nous regardons attentivement, il y a un fichier caché contenant une première carte d'accès. Il faut de nouveau utiliser stegcracker pour extraire le fichier contenant la clé (```the_payday_gang_wont_break_our_security```).</br>


Maintenant nous pouvons nous attaquer au serveur SMB. On doit comprendre ce qu'il y a dans le fichier. C'est du JSFuck, le résultat est encodé en hexa, puis en binaire et enfin en base62. On obtient le mot de passe pur le serveur SMB : ```access_cards_are_secure```.</br>
Nous regardons ce qu'il y a sur le serveur SMB et un dossier partagé attire notre attention.
![image](https://user-images.githubusercontent.com/73934639/174636140-305bfd00-da1f-4e66-8e48-619efc4707b9.png)</br>

On essaye de s'y connecter avec les identifiants trouvés précédemment :</br>

On y trouve une note et un fichier audio. En y appliquant un spectrogramme on y trouve le message : ```harvest_not_so_trusty_XD```

En regardant le code source de la page du complice, on y trouve le lien vers le coffre. On donne les cartes d'accès et on est dedans. On retire l'argent du coffre et on s'enfuit :</br>
![image](https://user-images.githubusercontent.com/73934639/174637955-6217067a-6ef9-4403-83a6-cf064d4c6142.png)</br>


Dans le code source de la page, on y trouve une balise "section" et dedans ce qui semble être un nom d'utilisateur et un mot de passe.
```html
<section>dallas:1_n33d_4_m3d1c_846</section>
```

On se connecte au serveur ssh avec. On trouve le 1er flag dans une note. On voit qu'on peut exécuter le programme en tant qu'un autre utilisateur ("chains").</br>
![image](https://user-images.githubusercontent.com/73934639/174638546-d6c77830-60d8-4aca-bcd1-3161d8865bd9.png)</br>

On utilise la technique de ```Library Hijacking``` pour lancer un shell en tant que "Chains" lors de l'import de la bibliothèque random.
On récupère le 2e flag. Chains peut exécuter vi en tant qu'admin. On jette un coup d'oeil sur [GTFOBins](https://gtfobins.github.io/gtfobins/vi/#sudo).

On est maintenant root. On a donc le dernier flag. Il est dans un fichier caché.


