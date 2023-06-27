<?php
  // If character is (, go up one floor
  // If character is ), go down one floor
  $input = file_get_contents("in.txt");
  $floor = 0;  
  for($i = 0; $i < strlen($input); $i++) {
    if($input[$i] == '(') {
      $floor++;
    } else {
      $floor--;
    }
  }
  echo "p1: $floor\n";
?>