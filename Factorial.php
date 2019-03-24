<form action="" method="POST">
Type a factorial:
<br><br>
<input type="text" name="number_entered" value=''/> <br><br>
<input type="submit" name="check" value="Factorial?"/><br><br>
</form>

<?php
$checkbutton= $_POST['check'];
$number= $_POST['number_entered'];

if ($checkbutton){
    $count = 1;
    $value = 1;
    while ($count <= $number){
        $value = $count * $value;
        $count = $count + 1;
    }
    echo"Factorial:" . " ". $value;
}

?>